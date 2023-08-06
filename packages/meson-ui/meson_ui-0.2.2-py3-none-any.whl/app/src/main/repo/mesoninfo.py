#!/user/bin/env python3
###################################################################################
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michaelbrockus@gmail.com>                                      #
#                                                                                 #
# LICENSE: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0                 #
#                                                                                 #
###################################################################################
from os import path
from .mesonscan import MesonInfoScanner
from .mesonread import MesonInfoReader


class MesonInfo:
    '''
        This works on getting the data from Meson 'intro-*.json' files.
        and feeds it to the data wrappers classes.
    '''

    def __init__(self, context = None):
        self._context = context
        self._scan = MesonInfoScanner(self._context)
        self._read = MesonInfoReader(self._context)
    # end of method

    def get_mesoninfo(self, value: str) -> any:
        if path.exists(self._context.get_builddir()):
            return self._read._read_mesoninfo(value)
        else:
            return 'null'

    def get_projectinfo(self, value: str) -> any:
        if path.exists(self._context.get_builddir()):
            return self._read._read_projectinfo(value)
        elif path.isfile(self._scan._get_scriptdir()):
            return self._scan._scan_projectinfo(value)
        else:
            return 'null'

    def get_targets(self, index: int, value: str) -> any:
        if path.exists(self._context.get_builddir()):
            info = self._read._read_targets(index, value)
            return info
        elif path.isfile(self._scan._get_scriptdir()):
            info = self._scan._scan_targets(index, value)
            return info
        else:
            return 'null'

    def get_benchmarks(self, index: int, value: str) -> any:
        if path.exists(self._context.get_builddir()):
            return self._read._read_benchmarks(index, value)
        elif path.isfile(self._scan._get_scriptdir()):
            return self._scan._scan_benchmarks(index, value)
        else:
            return 'null'

    def get_tests(self, index: int, value: str) -> any:
        if path.exists(self._context.get_builddir()):
            return self._read._read_tests(index, value)
        elif path.isfile(self._scan._get_scriptdir()):
            return self._scan._scan_tests(index, value)
        else:
            return 'null'

    def get_targets_sources(self, index: int, value: str) -> any:
        if path.exists(self._context.get_builddir()):
            return self._read._read_targets_sources(index, value)
        elif path.isfile(self._scan._get_scriptdir()):
            return self._scan._scan_targets_sources(index, value)
        else:
            return 'null'

    def get_option(self, index: int, value: str):
        if path.exists(self._context.get_builddir()):
            return self._read._read_buildoptions(index, value)
        elif path.isfile(self._scan._get_scriptdir()):
            return self._scan._scan_buildoptions(index, value)
        else:
            return 'null'
