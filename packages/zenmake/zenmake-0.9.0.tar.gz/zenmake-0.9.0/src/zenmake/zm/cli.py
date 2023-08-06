# coding=utf-8
#

"""
 Copyright (c) 2019, Alexander Magola. All rights reserved.
 license: BSD 3-Clause License, see LICENSE for more details.
"""

import os
import sys
from collections import namedtuple, defaultdict

# argparse from the https://pypi.org/project/argparse/ supports alieses
from auxiliary.argparse import argparse
from zm.constants import APPNAME, CAP_APPNAME, PLATFORM
from zm.pyutils import maptype, viewitems
from zm import log
from zm.error import ZenMakeLogicError
from zm.autodict import AutoDict as _AutoDict

ParsedCommand = namedtuple('ParsedCommand', 'name, args')

"""
Object of ParsedCommand with current command after last parsing of command line
"""
selected = None

class _Command(_AutoDict):
    def __init__(self, *args, **kwargs):
        super(_Command, self).__init__(*args, **kwargs)
        self.setdefault('aliases', [])
        self.setdefault('usageTextTempl', "%s [options]")

# Declarative list of commands in CLI
_commands = [
    _Command(
        name = 'help',
        description = 'show help for a given topic or a help overview',
        usageTextTempl = "%s [command/topic]",
    ),
    _Command(
        name = 'configure',
        aliases = ['cnf'],
        description = 'configure project',
    ),
    _Command(
        name = 'build',
        aliases = ['bld'],
        description = 'build project',
        usageTextTempl = "%s [options] [task [task] ... ]",
    ),
    _Command(
        name = 'test',
        description = 'build and run tests',
        usageTextTempl = "%s [options] [task [task] ... ]",
    ),
    _Command(
        name = 'clean',
        aliases = ['c'],
        description = 'clean project',
    ),
    _Command(
        name = 'distclean',
        aliases = ['dc'],
        description = 'removes the build directory with everything in it',
    ),
    _Command(
        name = 'install',
        description = 'installs the targets on the system',
    ),
    _Command(
        name = 'uninstall',
        description = 'removes the targets installed',
    ),
    _Command(
        name = 'zipapp',
        description = 'make executable zip archive of %s' % APPNAME,
    ),
    _Command(
        name = 'version',
        aliases = ['ver'],
        description = 'print version of %s' % APPNAME,
    ),
    _Command(
        name = 'sysinfo',
        description = 'print some system info useful for diagnostic reasons',
    ),
]

# map: cmd name/alies -> _Command
def _makeCmdNameMap():
    cmdNameMap = {}
    for cmd in _commands:
        cmdNameMap[cmd.name] = cmd
        for alias in cmd.aliases:
            cmdNameMap[alias] = cmd
    return cmdNameMap

_cmdNameMap = _makeCmdNameMap()

class _PosArg(_AutoDict):

    NOTARGPARSE_FIELDS = ('name', 'commands')

# Declarative list of positional args after command name in CLI
_posargs = [
    # global options that are used before command in cmd line
    _PosArg(
        name = 'tasks',
        nargs = '*', # it means this arg is optional
        default = [],
        help = 'select tasks from buildconf, all tasks if nothing is selected',
        commands = ['build', 'test'],
    ),
]

class _Option(_AutoDict):

    NOTARGPARSE_FIELDS = ('names', 'commands', 'runcmd', 'isglobal')

    def __init__(self, *args, **kwargs):
        super(_Option, self).__init__(*args, **kwargs)
        self.setdefault('isglobal', False)
        self.setdefault('commands', [])
        self.setdefault('action', 'store')
        self.setdefault('type', None)
        self.setdefault('choices', None)
        self.setdefault('default', None)

# Declarative list of options in CLI
# Special param 'runcmd' is used to declare option that runs another command
# before current. There is no need to set 'action' in that case. And it can not
# be used for global options, of course.
_options = [
    # global options that are used before command in cmd line
    _Option(
        names = ['-h', '--help'],
        isglobal = True,
        action = 'help',
        help = 'show this help message and exit',
    ),
    # command options
    _Option(
        names = ['-h', '--help'],
        action = 'help',
        commands = [x.name for x in _commands], # for all commands
        help = 'show this help message for command and exit',
    ),
    _Option(
        names = ['-b', '--buildtype'],
        commands = ['configure', 'build', 'clean', 'test', 'install', 'uninstall'],
        help = 'set the build type',
    ),
    _Option(
        names = ['-g', '--configure'],
        commands = ['build', 'test', 'install'],
        runcmd = 'configure',
    ),
    _Option(
        names = ['-c', '--clean'],
        commands = ['build', 'test', 'install'],
        runcmd = 'clean',
    ),
    _Option(
        names = ['-d', '--distclean'],
        commands = ['configure', 'build', 'test', 'install'],
        runcmd = 'distclean',
    ),
    _Option(
        names = ['-t', '--build-tests'],
        dest = 'buildTests',
        choices = ('yes', 'no'),
        commands = ['build', 'test'],
        help = 'build tests',
    ),
    _Option(
        names = ['-T', '--run-tests'],
        dest = 'runTests',
        choices = ('all', 'on-changes', 'none'),
        commands = ['build', 'test'],
        help = 'run tests',
    ),
    _Option(
        names = ['-j', '--jobs'],
        type = int,
        commands = ['build', 'test', 'install'],
        help = 'amount of parallel jobs',
    ),
    _Option(
        names = ['-p', '--progress'],
        action = "store_true",
        commands = ['build', 'test', 'install', 'uninstall'],
        help = 'progress bar',
    ),
    _Option(
        names = ['--destdir'],
        commands = ['zipapp', 'install', 'uninstall'],
        help = 'destination directory',
    ),
    _Option(
        names = ['-o', '--buildroot'],
        commands = ['configure', 'build', 'test', 'clean',
                    'distclean', 'install', 'uninstall'],
        help = "build directory for the project",
    ),
    _Option(
        names = ['--prefix'],
        commands = ['configure', 'build', 'install', 'uninstall'],
        help = 'installation prefix',
    ),
    _Option(
        names = ['--bindir'],
        commands = ['configure', 'build', 'install', 'uninstall'],
        help = 'installation bin directory [ ${PREFIX}/bin ]',
    ),
    _Option(
        names = ['--libdir'],
        commands = ['configure', 'build', 'install', 'uninstall'],
        help = 'installation lib directory [ ${PREFIX}/lib[64] ]',
    ),
    _Option(
        names = ['-v', '--verbose'],
        action = "count",
        commands = [x.name for x in _commands if x.name != 'help'],
        help = 'verbosity level -v -vv or -vvv',
    ),
    _Option(
        names = ['--color'],
        choices = ('yes', 'no', 'auto'),
        commands = [x.name for x in _commands \
                            if x.name not in ('version', 'sysinfo')],
        help = 'whether to use colors (yes/no/auto)',
    ),
]

COMMAND_NAMES = ( x.name for x in _commands )
OPTION_NAMES = ( x.names[-1].replace('-', '', 2) for x in _options )

DEFAULT_PREFIX = '/usr/local/'
if PLATFORM == 'windows':
    import tempfile
    d = tempfile.gettempdir()
    # windows preserves the case, but gettempdir does not
    DEFAULT_PREFIX = d[0].upper() + d[1:]

def _getReadyOptDefaults():
    return {
        'verbose': 0,
        'color': os.environ.get('NOCOLOR', '') and 'no' or 'auto',
        'build-tests': { 'any': 'no',   'test' : 'yes' },
        'run-tests'  : { 'any': 'none', 'test' : 'all' },
        'destdir' : {
            'any': os.environ.get('DESTDIR', ''),
            'zipapp' : os.environ.get('DESTDIR', '.'),
        },
        'buildroot' : os.environ.get('BUILDROOT', None),
        'prefix' : os.environ.get('PREFIX', '') or DEFAULT_PREFIX,
        'bindir' : os.environ.get('BINDIR', None),
        'libdir' : os.environ.get('LIBDIR', None),
    }

class CmdLineParser(object):
    """
    CLI for ZenMake.
    WAF has own CLI and I could use it but I wanted to have a different CLI.
    """

    __slots__ = (
        '_defaults', '_options', '_command', '_wafCmdLine',
        '_parser', '_commandHelps'
    )

    def __init__(self, progName, defaults):

        self._defaults = defaultdict(dict)
        self._defaults.update(_getReadyOptDefaults())
        self._defaults.update(defaults)

        self._options = []
        self._command = None
        self._wafCmdLine = []

        self._setupOptions()

        class MyHelpFormatter(argparse.HelpFormatter):
            """ Some customization"""
            def __init__(self, prog):
                super(MyHelpFormatter, self).__init__(prog,
                                                      max_help_position = 27)
                self._action_max_length = 23

        kwargs = dict(
            prog = progName,
            formatter_class = MyHelpFormatter,
            description = '%s: build system based on the Waf build system' % CAP_APPNAME,
            usage = "%(prog)s <command> [options] [args]",
            add_help = False
        )
        self._parser = argparse.ArgumentParser(**kwargs)

        groupGlobal = self._parser.add_argument_group('global options')
        self._addOptions(groupGlobal, cmd = None)

        kwargs = dict(
            title = 'list of commands',
            help = '', metavar = '', dest = 'command'
        )
        subparsers = self._parser.add_subparsers(**kwargs)

        commandHelps = _AutoDict()
        helpCmd = None
        for cmd in _commands:
            commandHelps[cmd.name] = _AutoDict()
            cmdHelpInfo = commandHelps[cmd.name]
            cmdHelpInfo.usage = self._makeCmdUsageText(progName, cmd)
            cmdHelpInfo.help = cmd.description
            cmdHelpInfo.description = cmd.description.capitalize()
            cmdHelpInfo.aliases = cmd.aliases

            if cmd.name == 'help': # It will be processed below
                helpCmd = cmd
                continue

            kwargs = cmdHelpInfo
            kwargs['add_help'] = False
            cmdParser = subparsers.add_parser(cmd.name, **kwargs)

            self._addCmdPosArgs(cmdParser, cmd)

            groupCmdOpts = cmdParser.add_argument_group('command options')
            self._addOptions(groupCmdOpts, cmd = cmd)
            cmdHelpInfo.help = cmdParser.format_help()

        # special case for 'help' command
        if helpCmd is None:
            raise ZenMakeLogicError("Programming error: no command "
                                    "'help' in _commands") # pragma: no cover
        cmd = helpCmd
        kwargs = commandHelps[cmd.name]
        kwargs['add_help'] = True
        cmdParser = subparsers.add_parser(cmd.name, **kwargs)
        cmdParser.add_argument('topic', nargs='?', default = 'overview')

        self._commandHelps = commandHelps

    def _setupOptions(self):
        self._options = []

        # make independent copy
        for opt in _options:
            self._options.append(_Option(opt))

    def _getOptionDefault(self, opt, cmd  = None):
        optName = opt.names[-1].replace('-', '', 2)
        val = self._defaults.get(optName, None)
        if isinstance(val, maptype):
            cmd = 'any' if cmd is None else cmd.name
            val = val.get(cmd, val.get('any', None))
        return val

    @staticmethod
    def _joinCmdNameWithAlieses(cmd):
        if not cmd.aliases:
            return cmd.name
        return cmd.name + '|' + '|'.join(cmd.aliases)

    @staticmethod
    def _makeCmdUsageText(progName, cmd):
        template = "%s " + cmd.usageTextTempl
        return template % (progName, CmdLineParser._joinCmdNameWithAlieses(cmd))

    def _showHelp(self, cmdHelps, topic):
        if topic == 'overview':
            self._parser.print_help()
            return True

        _topic = _cmdNameMap.get(topic, None)
        if _topic:
            _topic = _topic.name

        if _topic is None or _topic not in cmdHelps:
            log.error("Unknown command/topic to show help: '%s'" % topic)
            return False

        print(cmdHelps[_topic]['help'])
        return True

    def _addCmdPosArgs(self, target, cmd):
        posargs = [x for x in _posargs if cmd.name in x.commands]
        for arg in posargs:
            kwargs = _AutoDict()
            for k, v in viewitems(arg):
                if v is None or k in _PosArg.NOTARGPARSE_FIELDS:
                    continue
                kwargs[k] = v
            target.add_argument(arg.name, **kwargs)

    def _addOptions(self, target, cmd = None):
        if cmd is None:
            # get only global options
            options = [x for x in self._options if x.isglobal]
        else:
            def isvalid(opt):
                if opt.isglobal:
                    return False
                return cmd.name in opt.commands
            options = [x for x in self._options if isvalid(x)]

        for opt in options:
            kwargs = _AutoDict()
            if 'runcmd' in opt:
                kwargs.action = "store_true"
                kwargs.help = "run command '%s' before command '%s'" \
                        % (opt.runcmd, cmd.name)
            else:
                for k, v in viewitems(opt):
                    if v is None or k in _Option.NOTARGPARSE_FIELDS:
                        continue
                    kwargs[k] = v
                default = self._getOptionDefault(opt, cmd)
                if default is not None:
                    kwargs['default'] = default
                    kwargs['help'] += ' [default: %r]' % kwargs['default']

            target.add_argument(*opt.names, **kwargs)

    def _postParse(self, parsedArgs):
        if hasattr(parsedArgs, 'buildTests'):
            parsedArgs.buildTests = parsedArgs.buildTests == 'yes'

    def _fillCmdInfo(self, parsedArgs):
        args = _AutoDict(vars(parsedArgs))
        cmd = _cmdNameMap[args.pop('command')]
        self._command = ParsedCommand(
            name = cmd.name,
            args = args,
        )

    def _fillWafCmdLine(self):
        if self._command is None:
            raise ZenMakeLogicError("Programming error: _command is None") # pragma: no cover

        # NOTE: The option/command 'distclean' is handled in special way

        cmdline = [self._command.name]

        # self._command.args is AutoDict and it means that it'll create
        # nonexistent keys in it, so we need to make copy
        options = _AutoDict(self._command.args)

        if self._command.name == 'test':
            # command 'test' should be always in pair with 'build'
            cmdline.insert(0, 'build')
        elif self._command.name == 'build':
            runTests = options.get('runTests', None)
            if runTests is not None and runTests != 'none':
                cmdline.append('test')

        if options.configure:
            cmdline.insert(0, 'configure')
        if options.clean:
            cmdline.insert(0, 'clean')
        if options.distclean:
            cmdline.insert(0, 'distclean')
        if options.progress:
            cmdline.append('--progress')
        if options.verbose:
            cmdline.append('-' + options.verbose * 'v')
        for opt in ('jobs', 'color', 'destdir', 'prefix', 'bindir', 'libdir'):
            val = options.get(opt)
            if val:
                cmdline.append('--%s=%s' % (opt, str(val)))

        self._wafCmdLine = cmdline

    def parse(self, args = None, defaultCmd = 'help'):
        """ Parse command line args """

        if args is None:
            args = sys.argv[1:]

        # simple hack to set default command
        if not args or not [ x for x in args if not x.startswith('-') ]:
            optHelp = _options[0]
            assert optHelp.action == 'help'
            # don't show help for default command
            if not any(x in optHelp.names for x in args):
                args.insert(0, defaultCmd)

        # parse
        args = self._parser.parse_args(args)
        cmd = _cmdNameMap[args.command]
        self._postParse(args)

        if cmd.name == 'help':
            self._fillCmdInfo(args)
            sys.exit(not self._showHelp(self._commandHelps, args.topic))

        self._fillCmdInfo(args)
        self._fillWafCmdLine()
        return self._command

    @property
    def command(self):
        """ current command after last parsing of command line"""
        return self._command

    @property
    def wafCmdLine(self):
        """
        current command line args for WAF command after last
        parsing of command line
        """
        return self._wafCmdLine

def parseAll(args, noBuildConf = True, defaults = None):
    """
    Parse all command line args with CmdLineParser and save selected
    command as object of ParsedCommand in global var 'selected' of this module.
    Returns selected command as object of ParsedCommand and parser.wafCmdLine
    """

    # simple hack for default behavior if command is not defined
    defaultCmd = 'help' if noBuildConf else 'build'

    if defaults is None:
        defaults = {}
    parser = CmdLineParser(APPNAME, defaults)
    cmd = parser.parse(args[1:], defaultCmd)

    return cmd, parser.wafCmdLine
