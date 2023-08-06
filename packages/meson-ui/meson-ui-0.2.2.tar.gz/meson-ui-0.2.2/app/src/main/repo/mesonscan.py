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
import json
import subprocess
from os.path import join as join_paths


class MesonInfoScanner:
    def __init__(self, context = None):
        self._context = context
    # end of method

    def _introspect(self, args):
        cmd = ['meson', 'introspect']
        cmd.extend(args)
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT)

    def _get_scriptdir(self):
        return join_paths(self._context.get_sourcedir(), 'meson.build')

    def _scan_projectinfo(self, value):
        info = json.loads(self._introspect(['--projectinfo', self._get_scriptdir()]))
        return info[value]

    def _scan_targets(self, index, value):
        info = json.loads(self._introspect(['--targets', self._get_scriptdir()]))
        return info[index][value]

    def _scan_targets_sources(self, index, value):
        info = json.loads(self._introspect(['--targets', self._get_scriptdir()]))
        return info[index]['target_sources'][index][value]

    def _scan_benchmarks(self, index, value):
        info = json.loads(self._introspect(['--benchmarks', '--force-object', self._get_scriptdir()]))
        if info == {}:
            return 'null'
        else:
            return info[index][value]

    def _scan_tests(self, index, value):
        info = json.loads(self._introspect(['--tests', '--force-object', self._get_scriptdir()]))
        if info == {}:
            return 'null'
        else:
            return info[index][value]

    def _scan_buildoptions(self, index, value):
        info = json.loads(self._introspect(['--buildoptions', self._get_scriptdir()]))
        return info[index][value]
