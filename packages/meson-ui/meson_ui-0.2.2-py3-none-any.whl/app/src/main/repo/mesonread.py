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
from os.path import join as join_paths
from os import path


class MesonInfoReader:
    def __init__(self, context = None):
        self._context = context
    # end of method

    def _meson_info_dir(self) -> str:
        return join_paths(f'{self._context.get_builddir()}', 'meson-info', 'meson-info.json')

    def _load_data(self, key: str) -> any:
        info_path = self._meson_info_dir()
        if not path.exists(info_path):
            return 'null'
        with open(info_path, 'r') as f:
            data = json.load(f)
        return data["introspection"]["information"][key]["file"]

    def _load_infodir(self) -> list:
        info_path = self._meson_info_dir()
        if not path.exists(info_path):
            return 'null'
        else:
            with open(info_path, 'r') as f:
                info = json.load(f)
        return info["directories"]["info"]

    def _read_mesoninfo(self, value):
        info_path = self._meson_info_dir()
        if not path.exists(info_path):
            return 'null'
        with open(info_path, 'r') as f:
            info = json.load(f)
        return info['meson_version'][value]

    def _read_projectinfo(self, value):
        info_path = join_paths(self._load_infodir(), self._load_data('projectinfo'))
        if not path.exists(info_path):
            return 'null'
        else:
            with open(info_path, 'r') as f:
                info = json.load(f)
        return info[value]

    def _read_targets(self, index, value):
        info_path = join_paths(self._load_infodir(), self._load_data('targets'))
        if not path.exists(info_path):
            return 'null'
        else:
            with open(info_path, 'r') as f:
                info = json.load(f)
        return info[index][value]

    def _read_targets_sources(self, index, value):
        info_path = join_paths(self._load_infodir(), self._load_data('targets'))
        if not path.exists(info_path):
            return 'null'
        else:
            with open(info_path, 'r') as f:
                info = json.load(f)
        if info == []:
            return 'null'
        else:
            return info[index]['target_sources'][index][value]

    def _read_benchmarks(self, index, value):
        info_path = join_paths(self._load_infodir(), self._load_data('benchmarks'))
        if not path.exists(info_path):
            return 'null'
        with open(info_path, 'r') as f:
            info = json.load(f)
        if info == []:
            return 'null'
        else:
            return info[index][value]

    def _read_tests(self, index, value):
        info_path = join_paths(self._load_infodir(), self._load_data('tests'))
        if not path.exists(info_path):
            return 'null'
        with open(info_path, 'r') as f:
            info = json.load(f)
        if info == []:
            return 'null'
        else:
            return info[index][value]

    def _read_buildoptions(self, index, value):
        info_path = join_paths(self._load_infodir(), self._load_data('buildoptions'))
        if not path.exists(info_path):
            return 'null'
        else:
            with open(info_path, 'r') as f:
                info = json.load(f)
        return info[index][value]
