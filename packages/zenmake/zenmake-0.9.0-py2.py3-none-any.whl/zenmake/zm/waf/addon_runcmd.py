# coding=utf-8
#

"""
 Copyright (c) 2019, Alexander Magola. All rights reserved.
 license: BSD 3-Clause License, see LICENSE for more details.

 This module adds Waf feature 'runcmd' in tasks
"""

import os
import shlex

from waflib.TaskGen import feature, after
from waflib.Errors import WafError
from waflib import Task
from zm.pyutils import viewitems
from zm import log, error
from zm.constants import PLATFORM, EXE_FILE_EXTS
from zm.waf.addons import postcmd

if PLATFORM == 'windows':
    CMDFILE_EXTS = EXE_FILE_EXTS + '.py,.pl'
else:
    CMDFILE_EXTS = EXE_FILE_EXTS

@postcmd('options')
def postOpt(ctx):
    """ Extra init after wscript.options """

    ctx.validUserTaskFeatures.add('runcmd')

def _processCmdLine(conf, cwd, shell, cmdArgs):
    """ Get and process 'cmd' at 'configure' stage """

    bconf      = conf.getbconf()
    bconfPaths = bconf.confPaths
    btypeDir   = bconf.selectedBuildTypeDir
    startdir   = bconfPaths.startdir

    cmdline = cmdArgs.get('cmd', '').strip()
    if not cmdline:
        return cmdline, shell

    if not shell:
        if any(s in cmdline for s in ('<', '>', '&&')):
            shell = True

    cmdSplitted = shlex.split(cmdline)

    if not shell:
        # Waf can not work correctly with paths with whitespaces when
        # 'shell' is False.
        # TODO: try to make solution for 'shell' == False
        if any(' ' in s for s in cmdSplitted):
            shell = True

    paths = [cwd, startdir, btypeDir]
    paths.extend(os.environ.get('PATH', '').split(os.pathsep))
    fkw = dict(
        path_list = paths, quiet = True,
        exts = CMDFILE_EXTS, mandatory = False
    )

    partsCount = len(cmdSplitted)
    cmdExt = os.path.splitext(cmdSplitted[0])[1]
    if partsCount == 1 and cmdExt:
        # try to detect interpreter for some cases
        for ext, launcher in ( ('.py', 'python'), ('.pl', 'perl'),):
            if cmdExt != ext:
                continue
            result = conf.find_program(launcher, **fkw)
            if result:
                launcher = result[0]
                cmdline = '%s %s' % (launcher, cmdline)
    elif partsCount > 1 and not shell:
        # Waf raises exception in verbose mode with 'shell' == False if it
        # cannot find full path to executable and on windows cmdline
        # like 'python file.py' doesn't work.
        # So here is trying to find full path for such cases.
        launcher = cmdSplitted[0]
        result = conf.find_program(launcher, **fkw)
        if result:
            launcher = result[0]
            cmdSplitted[0] = launcher
            cmdSplitted = [ x.replace(r'"', r'\"') for x in cmdSplitted]
            cmdline = ' '.join('"%s"' % s if ' ' in s else s for s in cmdSplitted)

    return cmdline, shell

@postcmd('configure')
def postConf(conf):
    """ Prepare task params after wscript.configure """

    bconf      = conf.getbconf()
    btypeDir   = bconf.selectedBuildTypeDir
    rootdir    = bconf.rootdir
    tasks      = bconf.tasks

    for taskName, taskParams in viewitems(tasks):
        features = taskParams['features']
        cmdArgs = taskParams.get('run', None)

        if 'runcmd' not in features:
            if cmdArgs is not None:
                features.append('runcmd')
            else:
                continue

        if cmdArgs is None:
            cmdArgs = {}

        cmdTaskArgs = dict(
            name     = taskName,
            timeout  = cmdArgs.get('timeout', None),
            env      = cmdArgs.get('env', {}),
            repeat   = cmdArgs.get('repeat', 1),
        )

        cwd = cmdArgs.get('cwd', None)
        if cwd:
            startdir = cmdArgs.get('startdir', bconf.startdir)
            if not os.path.isabs(cwd):
                if not os.path.isabs(startdir):
                    startdir = os.path.join(rootdir, startdir)
                cwd = os.path.join(startdir, cwd)
            cwd = conf.root.make_node(cwd).abspath()
        else:
            cwd = btypeDir
        cmdTaskArgs['cwd'] = cwd

        cmdTaskArgs['$type'] = ''
        cmd = cmdArgs.get('cmd', None)
        if cmd and callable(cmd):
            # it's needed because Waf cannot save function in file as is
            cmdTaskArgs['cmd'] = cmd.__name__
            cmdTaskArgs['shell'] = False
            cmdTaskArgs['$type'] = 'func'
        else:
            # By default 'shell' is True to rid of some problems with Waf and Windows
            shell = cmdArgs.get('shell', True)
            cmd, shell = _processCmdLine(conf, cwd, shell, cmdArgs)
            cmdTaskArgs['shell'] = shell
            cmdTaskArgs['cmd'] = cmd

        taskParams['run'] = cmdTaskArgs

def _fixRunCmdDepsOrder(tgen):
    """ Fix order of running """

    ctx = tgen.bld
    runcmdTask = getattr(tgen, 'runcmdTask', None)
    assert runcmdTask

    linkTask = getattr(tgen, 'link_task', None)
    if linkTask:
        runcmdTask.set_run_after(linkTask)

    for dep in getattr(tgen, 'use', []):
        try:
            other = ctx.get_tgen_by_name(dep)
        except WafError:
            continue

        # Ensure that the other task generator has created its tasks
        other.post()

        _runcmdTask = getattr(other, 'runcmdTask', None)
        if _runcmdTask:
            runcmdTask.set_run_after(_runcmdTask)
            continue

        linkTask = getattr(other, 'link_task', None)
        if linkTask:
            runcmdTask.set_run_after(linkTask)

def _isCmdStandalone(tgen):
    """ Detect is current runcmd standalone """
    features = getattr(tgen, 'features', [])
    otherFeatures = set(features) - set(('runcmd', ))
    return not otherFeatures and not hasattr(tgen, 'rule')

def _createRunCmdTask(tgen, ruleArgs):
    """ Create new rule task for runcmd """

    classParams = dict(
        shell = ruleArgs['shell'],
        func  = ruleArgs['rule'],
        color = ruleArgs['color'],
    )

    name = '%s[runcmd]' % tgen.name
    cls = Task.task_factory(name, **classParams)

    setattr(cls, '__str__', lambda _: 'command for task %r' % tgen.name)
    setattr(cls, 'keyword', ruleArgs['cls_keyword'])
    if ruleArgs.get('deep_inputs', False):
        Task.deep_inputs(cls)

    task = tgen.create_task(name)
    for k in ('after', 'before', 'ext_in', 'ext_out'):
        setattr(task, k, ruleArgs.get(k, []))
    for k in ('timeout', 'cwd', 'env'):
        setattr(task, k, ruleArgs[k])

    return task

def _createRuleWithFunc(bconf, funcName):

    bconfPaths  = bconf.confPaths
    func = bconf.getattr(funcName)[0]

    def runFunc(task):
        tgen = task.generator
        zmTaskParams = getattr(tgen, 'zm-task-params', {})
        args = {
            'taskname'  : tgen.name,
            'startdir'  : bconfPaths.startdir,
            'buildroot' : bconfPaths.buildroot,
            'buildout'  : bconfPaths.buildout,
            'buildtype' : bconf.selectedBuildType,
            'target'    : zmTaskParams.get('$real.target', ''),
            'waftask'   : task,
        }
        func(args)

    return runFunc

@feature('runcmd')
@after('process_rule', 'apply_link')
def applyRunCmd(tgen):
    """ Apply feature 'runcmd' """

    ctx = tgen.bld

    zmTaskParams = getattr(tgen, 'zm-task-params', {})
    assert zmTaskParams

    cmdArgs = zmTaskParams.get('run', {})
    if not cmdArgs:
        return

    isStandalone = _isCmdStandalone(tgen)

    cmd = cmdArgs.pop('cmd', None)
    cmdType = cmdArgs.pop('$type', '')
    realTarget = zmTaskParams['$real.target']

    env = ctx.env.derive()
    env.env = dict(env.env or os.environ)
    env.env.update(cmdArgs.pop('env', {}))

    # add new var to use in 'rule'
    env['PROGRAM'] = realTarget

    ruleArgs = cmdArgs.copy()
    ruleArgs.update(dict(
        env   = env,
        color = getattr(tgen, 'color', 'BLUE'),
        cls_keyword = lambda _: 'Running',
        cls_str = lambda _: 'command %r' % tgen.name,
    ))
    repeat = ruleArgs.pop('repeat', 1)

    deepInputs = zmTaskParams.get('deep_inputs', False) or \
                            getattr(tgen, 'deep_inputs', False)
    if deepInputs:
        ruleArgs['deep_inputs'] = True

    if not cmd and zmTaskParams['$runnable']:
        cmd = realTarget

    if not cmd:
        msg = 'Task %r has not runnable command: %r.' % (tgen.name, cmd)
        raise error.ZenMakeError(msg)

    if cmdType == 'func':
        ruleArgs['rule'] = _createRuleWithFunc(ctx.getbconf(), cmd)
    else:
        ruleArgs['rule'] = cmd

    if isStandalone:
        for k, v in viewitems(ruleArgs):
            setattr(tgen, k, v)
        if hasattr(tgen, 'target'):
            delattr(tgen, 'target')
        tgen.process_rule()
        delattr(tgen, 'rule')
        setattr(tgen, 'runcmdTask', tgen.tasks[0])
    else:
        task = _createRunCmdTask(tgen, ruleArgs)
        setattr(tgen, 'runcmdTask', task)

    def wrap(method, task, repeat):
        def execute():
            if repeat == 1:
                return method()
            ret = None
            msg  = "Running #"
            number = 0
            while number < repeat:
                log.info('%s%d' % (msg, number + 1),
                         extra = { 'c1': log.colors(task.color) } )
                ret = method()
                number += 1
            return ret
        return execute

    runcmdTask = tgen.runcmdTask
    runcmdTask.run = wrap(runcmdTask.run, runcmdTask, repeat)

    _fixRunCmdDepsOrder(tgen)
