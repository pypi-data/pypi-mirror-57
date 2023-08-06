# coding=utf-8
#

# pylint: skip-file

"""
 Copyright (c) 2019, Alexander Magola. All rights reserved.
 license: BSD 3-Clause License, see LICENSE for more details.
"""

import sys
import os
from copy import deepcopy
import pytest
import tests.common as cmn
from zm.constants import APPNAME, CAP_APPNAME
from zm import cli

class TestSuite(object):

    @pytest.fixture(autouse = True)
    def setup(self):
        self.defaults = { 'buildtype': 'somedebug' }
        self.parser = cli.CmdLineParser('test', self.defaults)

    def _parseHelpArgs(self, args, capsys):
        # CLI prints help and does exit
        with pytest.raises(SystemExit) as cm:
            self.parser.parse(args)
        captured = capsys.readouterr()
        return cm.value.code, captured.out, captured.err

    def _testMainHelpMsg(self, args, capsys):
        ecode, out, err = self._parseHelpArgs(args, capsys)

        assert not err
        assert ecode == 0
        assert CAP_APPNAME in out
        assert 'based on the Waf build system' in out
        assert self.parser.command is not None
        assert self.parser.command.name == 'help'
        assert self.parser.command.args == {'topic': 'overview'}
        assert self.parser.wafCmdLine == []

    def _assertAllsForCmd(self, cmdname, checks, baseExpectedArgs):

        for check in checks:
            expectedArgs = deepcopy(baseExpectedArgs)
            expectedArgs.update(check['expectedArgsUpdate'])

            def assertAll(cmd, parsercmd, wafcmdline):
                assert cmd is not None
                assert parsercmd is not None
                assert parsercmd == cmd
                assert cmd.name == cmdname
                assert cmd.args == expectedArgs
                if 'wafArgs' in check:
                    assert sorted(check['wafArgs']) == sorted(wafcmdline)

            # parser with explicit args
            cmd = self.parser.parse(check['args'])
            assertAll(cmd, self.parser.command, self.parser.wafCmdLine)

            # parser with args from sys.argv
            oldargv = sys.argv
            sys.argv = [APPNAME] + check['args']
            cmd = self.parser.parse()
            sys.argv = oldargv
            assertAll(cmd, self.parser.command, self.parser.wafCmdLine)

    def testEmpty(self, capsys):
        self._testMainHelpMsg([], capsys)

    def testHelp(self, capsys):
        self._testMainHelpMsg(['help'], capsys)

    def testHelpWrongTopic(self, capsys):
        args = ['help', 'qwerty']
        ecode, out, err = self._parseHelpArgs(args, capsys)
        assert not out
        assert 'Unknown command/topic' in err
        assert ecode != 0

    def testHelpForCmds(self, capsys):
        for cmd in cli._commands:
            args = ['help', cmd.name]
            ecode, out, err = self._parseHelpArgs(args, capsys)
            assert ecode == 0
            assert not err
            if cmd.name == 'help':
                assert 'show help' in out
            else:
                assert cmd.description.capitalize() in out

    def testCmdBuild(self):

        baseExpectedArgs = {
            'buildtype' : self.defaults['buildtype'],
            'jobs' : None,
            'configure': False,
            'color': 'auto',
            'clean': False,
            'progress': False,
            'distclean': False,
            'tasks': [],
            'verbose': 0,
            'buildTests': False,
            'runTests': 'none',
            'bindir' : None,
            'libdir' : None,
            'prefix' : cli.DEFAULT_PREFIX,
            'buildroot' : None,
        }

        CMDNAME = 'build'
        CMNOPTS = ['--color=auto', '--prefix=' + cli.DEFAULT_PREFIX]

        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-b', 'release'],
                expectedArgsUpdate = {'buildtype': 'release'},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--jobs', '22'],
                expectedArgsUpdate = {'jobs': 22},
                wafArgs = [CMDNAME, '--jobs=22'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
                wafArgs = [CMDNAME, '-v'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-vvv'],
                expectedArgsUpdate = {'verbose': 3},
                wafArgs = [CMDNAME, '-vvv'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--configure'],
                expectedArgsUpdate = {'configure': True},
                wafArgs = ['configure', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--clean'],
                expectedArgsUpdate = {'clean': True},
                wafArgs = ['clean', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--distclean'],
                expectedArgsUpdate = {'distclean': True},
                wafArgs = ['distclean', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--build-tests', 'yes'],
                expectedArgsUpdate = {'buildTests': True},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--run-tests', 'all'],
                expectedArgsUpdate = {'runTests': 'all'},
                wafArgs = [CMDNAME, 'test'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--run-tests', 'on-changes'],
                expectedArgsUpdate = {'runTests': 'on-changes'},
                wafArgs = [CMDNAME, 'test'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--progress'],
                expectedArgsUpdate = {'progress': True},
                wafArgs = [CMDNAME, '--progress'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--color', 'no'],
                expectedArgsUpdate = {'color': 'no'},
                wafArgs = [CMDNAME, '--color=no'] + CMNOPTS[1:],
            ),
            dict(
                args = [CMDNAME, 'sometask'],
                expectedArgsUpdate = {'tasks': ['sometask']},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, 'sometask', 'anothertask'],
                expectedArgsUpdate = {'tasks': ['sometask', 'anothertask']},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--buildroot', 'somedir'],
                expectedArgsUpdate = {'buildroot' : 'somedir'},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)

    def testCmdTest(self):

        baseExpectedArgs = {
            'buildtype' : self.defaults['buildtype'],
            'jobs' : None,
            'configure': False,
            'color': 'auto',
            'clean': False,
            'progress': False,
            'distclean': False,
            'tasks': [],
            'verbose': 0,
            'buildTests': True,
            'runTests': 'all',
            'buildroot' : None,
        }

        CMDNAME = 'test'
        CMNOPTS = ['--color=auto',]

        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
                wafArgs = ['build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-b', 'release'],
                expectedArgsUpdate = {'buildtype': 'release'},
                wafArgs = ['build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--jobs', '22'],
                expectedArgsUpdate = {'jobs': 22},
                wafArgs = ['build', CMDNAME, '--jobs=22'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
                wafArgs = ['build', CMDNAME, '-v'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-vvv'],
                expectedArgsUpdate = {'verbose': 3},
                wafArgs = ['build', CMDNAME, '-vvv'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--configure'],
                expectedArgsUpdate = {'configure': True},
                wafArgs = ['configure', 'build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--clean'],
                expectedArgsUpdate = {'clean': True},
                wafArgs = ['clean', 'build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--distclean'],
                expectedArgsUpdate = {'distclean': True},
                wafArgs = ['distclean', 'build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--build-tests', 'no'],
                expectedArgsUpdate = {'buildTests': False},
                wafArgs = ['build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--run-tests', 'none'],
                expectedArgsUpdate = {'runTests': 'none'},
                wafArgs = ['build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--run-tests', 'on-changes'],
                expectedArgsUpdate = {'runTests': 'on-changes'},
                wafArgs = ['build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--progress'],
                expectedArgsUpdate = {'progress': True},
                wafArgs = ['build', CMDNAME, '--progress'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--color', 'no'],
                expectedArgsUpdate = {'color': 'no'},
                wafArgs = ['build', CMDNAME, '--color=no'],
            ),
            dict(
                args = [CMDNAME, 'sometask'],
                expectedArgsUpdate = {'tasks': ['sometask']},
                wafArgs = ['build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, 'sometask', 'anothertask'],
                expectedArgsUpdate = {'tasks': ['sometask', 'anothertask']},
                wafArgs = ['build', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--buildroot', os.getcwd()],
                expectedArgsUpdate = {'buildroot' : os.getcwd()},
                wafArgs = ['build', CMDNAME] + CMNOPTS,
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)

    def testCmdConfigure(self):

        baseExpectedArgs = {
            'buildtype' : self.defaults['buildtype'],
            'color': 'auto',
            'distclean': False,
            'verbose': 0,
            'bindir' : None,
            'libdir' : None,
            'prefix' : cli.DEFAULT_PREFIX,
            'buildroot' : None,
        }

        CMDNAME = 'configure'
        CMNOPTS = ['--color=auto', '--prefix=' + cli.DEFAULT_PREFIX]

        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-b', 'release'],
                expectedArgsUpdate = {'buildtype': 'release'},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--distclean'],
                expectedArgsUpdate = {'distclean': True},
                wafArgs = ['distclean', CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
                wafArgs = [CMDNAME, '-v'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-vvv'],
                expectedArgsUpdate = {'verbose': 3},
                wafArgs = [CMDNAME, '-vvv'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--color', 'no'],
                expectedArgsUpdate = {'color': 'no'},
                wafArgs = [CMDNAME, '--color=no'] + CMNOPTS[1:],
            ),
            dict(
                args = [CMDNAME, '--buildroot', os.getcwd()],
                expectedArgsUpdate = {'buildroot' : os.getcwd()},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)

    def testCmdClean(self):

        baseExpectedArgs = {
            'buildtype' : self.defaults['buildtype'],
            'color': 'auto',
            'verbose': 0,
            'buildroot' : None,
        }

        CMDNAME = 'clean'
        CMNOPTS = ['--color=auto',]

        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-b', 'release'],
                expectedArgsUpdate = {'buildtype': 'release'},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
                wafArgs = [CMDNAME, '-v'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-vvv'],
                expectedArgsUpdate = {'verbose': 3},
                wafArgs = [CMDNAME, '-vvv'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--color', 'no'],
                expectedArgsUpdate = {'color': 'no'},
                wafArgs = [CMDNAME, '--color=no'],
            ),
            dict(
                args = [CMDNAME, '--buildroot', os.getcwd()],
                expectedArgsUpdate = {'buildroot' : os.getcwd()},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)

    def testCmdDistclean(self):

        baseExpectedArgs = {
            'color': 'auto',
            'verbose': 0,
            'buildroot' : None,
        }

        CMDNAME = 'distclean'
        CMNOPTS = ['--color=auto',]

        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
                wafArgs = [CMDNAME, '-v'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '-vvv'],
                expectedArgsUpdate = {'verbose': 3},
                wafArgs = [CMDNAME, '-vvv'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--color', 'no'],
                expectedArgsUpdate = {'color': 'no'},
                wafArgs = [CMDNAME, '--color=no'],
            ),
            dict(
                args = [CMDNAME, '--buildroot', os.getcwd()],
                expectedArgsUpdate = {'buildroot' : os.getcwd()},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)

    def testCmdZipApp(self):

        baseExpectedArgs = {
            'destdir' : '.',
            'color': 'auto',
            'verbose': 0,
        }

        CMDNAME = 'zipapp'
        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
            ),
            dict(
                args = [CMDNAME, '--destdir', 'somedir'],
                expectedArgsUpdate = {'destdir' : 'somedir'},
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
            ),
            dict(
                args = [CMDNAME, '--color', 'no'],
                expectedArgsUpdate = {'color': 'no'},
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)

    def checkCmdInstall(self, cmd):

        baseExpectedArgs = {
            'buildtype' : self.defaults['buildtype'],
            'jobs' : None,
            'color': 'auto',
            'configure': False,
            'clean': False,
            'progress': False,
            'distclean': False,
            'verbose': 0,
            'destdir' : '',
            'bindir' : None,
            'libdir' : None,
            'prefix' : cli.DEFAULT_PREFIX,
            'buildroot' : None,
        }

        if cmd == 'uninstall':
            for name in ('configure', 'jobs', 'clean', 'distclean'):
                baseExpectedArgs.pop(name)

        CMDNAME = cmd
        CMNOPTS = ['--color=auto', '--prefix=' + cli.DEFAULT_PREFIX]

        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--destdir', 'somedir'],
                expectedArgsUpdate = {'destdir' : 'somedir'},
                wafArgs = [CMDNAME, '--destdir=somedir'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--bindir', 'somedir'],
                expectedArgsUpdate = {'bindir' : 'somedir'},
                wafArgs = [CMDNAME, '--bindir=somedir'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--libdir', 'somedir'],
                expectedArgsUpdate = {'libdir' : 'somedir'},
                wafArgs = [CMDNAME, '--libdir=somedir'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
                wafArgs = [CMDNAME, '-v'] + CMNOPTS,
            ),
            dict(
                args = [CMDNAME, '--color', 'no'],
                expectedArgsUpdate = {'color': 'no'},
                wafArgs = [CMDNAME, '--color=no'] + CMNOPTS[1:],
            ),
            dict(
                args = [CMDNAME, '--buildroot', os.getcwd()],
                expectedArgsUpdate = {'buildroot' : os.getcwd()},
                wafArgs = [CMDNAME] + CMNOPTS,
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)

    def testCmdInstall(self):
        self.checkCmdInstall('install')

    def testCmdUninstall(self):
        self.checkCmdInstall('uninstall')

    def testCmdVersion(self):

        baseExpectedArgs = {
            'verbose': 0,
        }

        CMDNAME = 'version'
        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
                wafArgs = [CMDNAME],
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
                wafArgs = [CMDNAME, '-v'],
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)

    def testCmdSysInfo(self):

        baseExpectedArgs = {
            'verbose': 0,
        }

        CMDNAME = 'sysinfo'
        checks = [
            dict(
                args = [CMDNAME],
                expectedArgsUpdate = {},
                wafArgs = [CMDNAME],
            ),
            dict(
                args = [CMDNAME, '--verbose'],
                expectedArgsUpdate = {'verbose': 1},
                wafArgs = [CMDNAME, '-v'],
            ),
        ]

        self._assertAllsForCmd(CMDNAME, checks, baseExpectedArgs)
