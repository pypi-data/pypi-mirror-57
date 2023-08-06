# coding=utf-8
#

"""
 Copyright (c) 2019, Alexander Magola. All rights reserved.
 license: BSD 3-Clause License, see LICENSE for more details.
"""

import os
import sys
import re

from waflib import Utils as wafutils
from zm import pyutils as _pyutils

WINDOWS_RESERVED_FILENAMES = (
    'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5',
    'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5',
    'LPT6', 'LPT7', 'LPT8', 'LPT9'
)

def platform():
    """
    Return current system platfom. For MS Windows paltfrom is always 'windows'.
    """
    result = wafutils.unversioned_sys_platform()
    if result.startswith('win32'):
        result = 'windows' # pragma: no cover
    return result

PLATFORM = platform()

readFile           = wafutils.readf
hashOfStrs         = wafutils.h_list
hashOfFunc         = wafutils.h_fun
hexOfStr           = wafutils.to_hex
substVars          = wafutils.subst_vars
libDirPostfix      = wafutils.lib64
Timer              = wafutils.Timer
threading          = wafutils.threading

def normalizeForDefine(s):
    """
	Converts a string into an identifier suitable for C defines.
    """
    if s[0].isdigit():
        s = '_%s' % s
    return wafutils.quote_define_name(s)

def normalizeForFileName(s, spaceAsDash = False):
    """
    Convert a string into string suitable for file name
    """
    s = str(s).strip()
    if spaceAsDash:
        s = s.replace(' ', '-')
    else:
        s = s.replace(' ', '_')
    s = re.sub(r'(?u)[^-\w.]', '', s)
    if PLATFORM == 'windows' and s.upper() in WINDOWS_RESERVED_FILENAMES:
        s = '_%s' % s
    return s

def toList(val):
    """
    Converts a string argument to a list by splitting it by spaces.
    Returns the object if not a string
    """
    if isinstance(val, _pyutils.stringtype):
        return val.split()
    return val

def uniqueListWithOrder(lst):
    """
    Return new list with preserved the original order of the list
    """
    used = set()
    return [x for x in lst if x not in used and (used.add(x) or True)]

def unfoldPath(cwd, path):
    """
    Unfold path applying os.path.expandvars, os.path.expanduser and
    os.path.abspath
    """
    if not path:
        return path

    if not os.path.isabs(path):
        path = os.path.join(cwd, path)

    path = os.path.expandvars(path)
    path = os.path.expanduser(path)
    path = os.path.abspath(path) # abspath returns normalized absolutized version
    return path

def getNativePath(path):
    """
    Return native path from POSIX path
    """
    if not path:
        return path
    return path.replace('/', os.sep) if os.sep != '/' else path

def mksymlink(src, dst, force = True):
    """
    Make symlink, force delete if destination exists already
    """
    if force and (os.path.exists(dst) or os.path.lexists(dst)):
        os.unlink(dst)

    _mksymlink = getattr(os, "symlink", None)
    if callable(_mksymlink):
        _mksymlink(src, dst)
        return

    raise NotImplementedError

def _loadPyModuleWithoutImport(name):

    # In this case we should compile python file manually
    # WARN: It has no support for all python module attributes.

    import types
    from zm.error import ZenMakeError
    from zm.pypkg import PkgPath
    joinpath = os.path.join

    module = types.ModuleType(name)
    filename = name.replace('.', os.path.sep)

    # try to find module
    isPkg = False
    for path in sys.path:
        modulePath = joinpath(path, filename)
        path = PkgPath(modulePath + '.py')
        if path.isfile():
            modulePath = path
            break
        path = PkgPath(joinpath(modulePath, '__init__.py'))
        if path.isfile():
            modulePath = path
            isPkg = True
            break
    else:
        raise ImportError('File %r not found' % filename)

    try:
        code = modulePath.read()
    except EnvironmentError:
        raise ZenMakeError('Could not read the file %r' % str(modulePath))

    module.__file__ = modulePath.path

    #pylint: disable=exec-used
    exec(compile(code, modulePath.path, 'exec'), module.__dict__)

    # From https://docs.python.org/3/reference/import.html:
    #
    # The module’s __package__ attribute should be set. Its value must be
    # a string, but it can be the same value as its __name__. If the attribute
    # is set to None or is missing, the import system will fill it in with
    # a more appropriate value. When the module is a package, its __package__
    # value should be set to its __name__. When the module is not a package,
    # __package__ should be set to the empty string for top-level modules, or
    # for submodules, to the parent package’s name.
    if isPkg:
        module.__package__ = name
    else:
        lastdotpos = name.rfind('.')
        module.__package__ = '' if lastdotpos < 0 else name[0:lastdotpos]
    return module

def loadPyModule(name, dirpath = None, withImport = True):
    """
    Load python module by name.
    Param 'dirpath' is optional param that is used to add/remove path into sys.path.
    Module is not imported (doesn't exist in sys.modules) if withImport is False.
    With withImport = False you should control where to store returned module object.
    """

    if withImport:
        import importlib
        loadModule = importlib.import_module
    else:
        loadModule = _loadPyModuleWithoutImport

    if dirpath:
        sys.path.insert(0, dirpath)
        try:
            module = loadModule(name)
        finally:
            sys.path.pop(0)
    else:
        module = loadModule(name)
    return module
