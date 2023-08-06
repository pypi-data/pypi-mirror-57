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
from PyQt5.QtCore import QObject, QProcess
from app.src.main.model.mesonuimodel import MesonUiModule
from app.src.main.mesonuilib.meson.meson import Meson
from os.path import exists as does_exists
from os.path import join as join_paths
from time import sleep
import unittest


test_case: map = {
    'case-01': 'test-cases/meson/01-setup-prog',
    'case-02': 'test-cases/meson/02-build-prog',
    'case-03': 'test-cases/meson/03-clean-prog',
    'case-04': 'test-cases/meson/04-test-prog',
    'case-05': 'test-cases/meson/05-install-prog',
    'case-06': 'test-cases/meson/06-dist-prog',
    'case-07': 'test-cases/meson/07-setup-error',
    'case-08': 'test-cases/meson/08-build-error',
    'case-09': 'test-cases/meson/09-clean-error',
    'case-10': 'test-cases/meson/10-test-error',
    'case-11': 'test-cases/meson/11-install-error',
    'case-12': 'test-cases/meson/12-dist-error',
    'case-13': 'test-cases/ninja/01-build-prog',
    'case-14': 'test-cases/ninja/02-clean-prog',
    'case-15': 'test-cases/ninja/03-test-prog',
    'case-16': 'test-cases/ninja/04-install-prog',
    'case-17': 'test-cases/ninja/05-dist-prog',
    'case-18': 'test-cases/ninja/06-build-error',
    'case-19': 'test-cases/ninja/07-clean-error',
    'case-20': 'test-cases/ninja/08-test-error',
    'case-21': 'test-cases/ninja/09-install-error',
    'case-22': 'test-cases/ninja/10-dist-error',
    'case-23': 'test-cases/intro/01-builddir-projectinfo',
    'case-24': 'test-cases/intro/02-builddir-targets',
    'case-25': 'test-cases/intro/03-builddir-targets-sources',
    'case-26': 'test-cases/intro/04-builddir-benchmarks',
    'case-27': 'test-cases/intro/05-builddir-tests',
    'case-28': 'test-cases/intro/06-builddir-mesoninfo',
    'case-29': 'test-cases/intro/07-scanner-projectinfo',
    'case-30': 'test-cases/intro/08-scanner-targets',
    'case-31': 'test-cases/intro/09-scanner-targets-sources',
    'case-32': 'test-cases/intro/10-scanner-benchmarks',
    'case-33': 'test-cases/intro/11-scanner-tests',
    'case-34': 'test-cases/intro/12-null-projectinfo',
    'case-35': 'test-cases/intro/13-null-targets',
    'case-36': 'test-cases/intro/14-null-targets-sources',
    'case-37': 'test-cases/intro/15-null-benchmarks',
    'case-38': 'test-cases/intro/16-null-tests',
    'case-39': 'test-cases/intro/17-null-mesoninfo',
}


# scanner  null
#
# This class is faking the apps projetc data
#
class FakeProg(QObject):
    def __init__(self):
        super().__init__()
        self._process = QProcess(self)
        self.dir_src = ''
        self.dir_build = ''

    def process(self):
        return self._process

    def set_sourcedir(self, value: str) -> str:
        self.dir_src = value

    def set_builddir(self, value: str) -> str:
        self.dir_build = value

    def get_sourcedir(self) -> str:
        return self.dir_src

    def get_builddir(self) -> str:
        return self.dir_build


class MesonWrapperTest(unittest.TestCase):
    def test_meson_setup(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-01'])
        prog.set_builddir(join_paths(test_case['case-01'], 'builddir'))

        meson = Meson(prog)
        meson.setup()

        sleep(1)

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_meson_build(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-02'])
        prog.set_builddir(join_paths(test_case['case-02'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_meson_clean(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-03'])
        prog.set_builddir(join_paths(test_case['case-03'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()
        meson.clean()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_meson_test(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-04'])
        prog.set_builddir(join_paths(test_case['case-04'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()
        meson.tests()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_meson_install(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-05'])
        prog.set_builddir(join_paths(test_case['case-05'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()
        meson.install()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_meson_dist(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-06'])
        prog.set_builddir(join_paths(test_case['case-06'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()
        meson.dist()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_meson_error_setup(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-07'])
        prog.set_builddir(join_paths(test_case['case-07'], 'builddir'))

        meson = Meson(prog)
        meson.setup()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_meson_error_build(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-08'])
        prog.set_builddir(join_paths(test_case['case-08'], 'builddir'))

        meson = Meson(prog)
        meson.build()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_meson_error_clean(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-09'])
        prog.set_builddir(join_paths(test_case['case-09'], 'builddir'))

        meson = Meson(prog)
        meson.clean()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_meson_error_test(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-10'])
        prog.set_builddir(join_paths(test_case['case-10'], 'builddir'))

        meson = Meson(prog)
        meson.tests()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_meson_error_install(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-11'])
        prog.set_builddir(join_paths(test_case['case-11'], 'builddir'))

        meson = Meson(prog)
        meson.install()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_meson_error_dist(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-12'])
        prog.set_builddir(join_paths(test_case['case-12'], 'builddir'))

        meson = Meson(prog)
        meson.dist()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())


class NinjaWrapperTest(unittest.TestCase):
    def test_ninja_build(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-13'])
        prog.set_builddir(join_paths(test_case['case-13'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson._ninja.build()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_ninja_clean(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-14'])
        prog.set_builddir(join_paths(test_case['case-14'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()
        meson._ninja.clean()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_ninja_test(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-15'])
        prog.set_builddir(join_paths(test_case['case-15'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()
        meson._ninja.test()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_ninja_install(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-16'])
        prog.set_builddir(join_paths(test_case['case-16'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()
        meson._ninja.install()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_ninja_dist(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-17'])
        prog.set_builddir(join_paths(test_case['case-17'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()
        meson._ninja.dist()

        assert does_exists(prog.get_sourcedir())
        assert does_exists(prog.get_builddir())

    def test_ninja_error_build(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-18'])
        prog.set_builddir(join_paths(test_case['case-18'], 'builddir'))

        meson = Meson(prog)
        meson._ninja.build()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_ninja_error_clean(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-19'])
        prog.set_builddir(join_paths(test_case['case-19'], 'builddir'))

        meson = Meson(prog)
        meson._ninja.clean()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_ninja_error_test(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-20'])
        prog.set_builddir(join_paths(test_case['case-20'], 'builddir'))

        meson = Meson(prog)
        meson._ninja.test()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_ninja_error_install(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-21'])
        prog.set_builddir(join_paths(test_case['case-21'], 'builddir'))

        meson = Meson(prog)
        meson._ninja.install()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())

    def test_ninja_error_dist(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-22'])
        prog.set_builddir(join_paths(test_case['case-12'], 'builddir'))

        meson = Meson(prog)
        meson._ninja.dist()

        assert does_exists(prog.get_sourcedir())
        assert not does_exists(prog.get_builddir())


class IntrospectTest(unittest.TestCase):
    def test_projectinfo_from_builddir(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-23'])
        prog.set_builddir(join_paths(test_case['case-23'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()

        meson_data: MesonUiModule = MesonUiModule(prog)

        #Testing project info
        assert meson_data.get_projectinfo().get_name() == 'c-exe'
        assert meson_data.get_projectinfo().get_version() == 'undefined'
        assert meson_data.get_projectinfo().get_subproject_dir(
        ) == 'subprojects'
        assert meson_data.get_projectinfo().get_subprojects() == []

    def test_targets_from_builddir(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-24'])
        prog.set_builddir(join_paths(test_case['case-24'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing targets info
        assert meson_data.get_targets().get_build_by_default() is True
        assert meson_data.get_targets().get_type() == 'executable'
        assert meson_data.get_targets().get_subproject() is None
        assert meson_data.get_targets().get_name() == 'exe'

    def test_targets_sources_from_builddir(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-25'])
        prog.set_builddir(join_paths(test_case['case-25'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing targets sources info
        assert meson_data.get_targets_sources().get_language() == 'c'

    def test_benchmarks_from_builddir(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-26'])
        prog.set_builddir(join_paths(test_case['case-26'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing benchmark info
        assert meson_data.get_benchmark().get_environment() == {}
        assert meson_data.get_benchmark().get_is_parallel() is True
        assert meson_data.get_benchmark().get_name() == 'Run benchmark exe'
        assert meson_data.get_benchmark().get_priority() == 0
        assert meson_data.get_benchmark().get_suite() == ['c-exe']
        assert meson_data.get_benchmark().get_timeout() == 30
        assert meson_data.get_benchmark().get_workdir() is None

    def test_tests_from_builddir(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-27'])
        prog.set_builddir(join_paths(test_case['case-27'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing test info
        assert meson_data.get_tests().get_environment() == {}
        assert meson_data.get_tests().get_is_parallel() is True
        assert meson_data.get_tests().get_name() == 'Run test exe'
        assert meson_data.get_tests().get_priority() == 0
        assert meson_data.get_tests().get_suite() == ['c-exe']
        assert meson_data.get_tests().get_timeout() == 30
        assert meson_data.get_tests().get_workdir() is None

    def test_mesoninfo_from_builddir(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-28'])
        prog.set_builddir(join_paths(test_case['case-28'], 'builddir'))

        meson = Meson(prog)
        meson.setup()
        meson.build()

        meson_data: MesonUiModule = MesonUiModule(prog)

        assert str(meson_data.get_mesoninfo().get_major_version()) == '0'
        assert str(meson_data.get_mesoninfo().get_minor_version()) in [
            '50', '51', '52', '53'
        ]
        assert str(meson_data.get_mesoninfo().get_full_version()) in [
            '0.50.0', '0.51.0', '0.52.0', '0.52.1', '0.53.0'
        ]
        assert str(
            meson_data.get_mesoninfo().get_patch_version()) in ['0', '1', '2']

    def test_projectinfo_from_scanner(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-29'])
        prog.set_builddir(join_paths(test_case['case-29'], 'builddir'))

        meson_data: MesonUiModule = MesonUiModule(prog)

        #Testing project info
        assert meson_data.get_projectinfo().get_name() == 'c-exe'
        assert meson_data.get_projectinfo().get_version() == 'undefined'
        assert meson_data.get_projectinfo().get_subproject_dir(
        ) == 'subprojects'
        assert meson_data.get_projectinfo().get_subprojects() == []

    def test_targets_from_scanner(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-30'])
        prog.set_builddir(join_paths(test_case['case-30'], 'builddir'))

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing targets info
        assert meson_data.get_targets().get_build_by_default() is True
        assert meson_data.get_targets().get_type() == 'executable'
        assert meson_data.get_targets().get_subproject() is None
        assert meson_data.get_targets().get_name() == 'exe'

    def test_targets_sources_from_scanner(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-31'])
        prog.set_builddir(join_paths(test_case['case-31'], 'builddir'))

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing targets sources info
        assert meson_data.get_targets_sources().get_language() == 'unknown'

    def test_benchmarks_from_scanner(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-32'])
        prog.set_builddir(join_paths(test_case['case-32'], 'builddir'))

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing benchmark info
        assert meson_data.get_benchmark().get_environment() == 'null'
        assert meson_data.get_benchmark().get_is_parallel() == 'null'
        assert meson_data.get_benchmark().get_name() == 'null'
        assert meson_data.get_benchmark().get_priority() == 'null'
        assert meson_data.get_benchmark().get_suite() == 'null'
        assert meson_data.get_benchmark().get_timeout() == 'null'
        assert meson_data.get_benchmark().get_workdir() == 'null'

    def test_tests_from_scanner(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-33'])
        prog.set_builddir(join_paths(test_case['case-33'], 'builddir'))

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing test info
        assert meson_data.get_tests().get_environment() == 'null'
        assert meson_data.get_tests().get_is_parallel() == 'null'
        assert meson_data.get_tests().get_name() == 'null'
        assert meson_data.get_tests().get_priority() == 'null'
        assert meson_data.get_tests().get_suite() == 'null'
        assert meson_data.get_tests().get_timeout() == 'null'
        assert meson_data.get_tests().get_workdir() == 'null'

    def test_projectinfo_as_null(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-34'])

        meson_data: MesonUiModule = MesonUiModule(prog)

        #Testing project info
        assert meson_data.get_projectinfo().get_name() == 'null'
        assert meson_data.get_projectinfo().get_version() == 'null'
        assert meson_data.get_projectinfo().get_subproject_dir() == 'null'
        assert meson_data.get_projectinfo().get_subprojects() == 'null'

    def test_targets_as_null(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-35'])

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing targets info
        assert meson_data.get_targets().get_build_by_default() == 'null'
        assert meson_data.get_targets().get_type() == 'null'
        assert meson_data.get_targets().get_subproject() == 'null'
        assert meson_data.get_targets().get_name() == 'null'

    def test_targets_sources_as_null(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-36'])

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing targets sources info
        assert meson_data.get_targets_sources().get_compiler() == 'null'
        assert meson_data.get_targets_sources().get_language() == 'null'
        assert meson_data.get_targets_sources().get_sources() == 'null'

        assert str(meson_data.get_mesoninfo().get_major_version()) == 'null'
        assert str(meson_data.get_mesoninfo().get_minor_version()) == 'null'
        assert str(meson_data.get_mesoninfo().get_full_version()) == 'null'
        assert str(meson_data.get_mesoninfo().get_patch_version()) == 'null'

    def test_benchmarks_as_null(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-37'])

        meson_data: MesonUiModule = MesonUiModule(prog)
        # Testing benchmark info
        assert meson_data.get_benchmark().get_environment() == 'null'
        assert meson_data.get_benchmark().get_is_parallel() == 'null'
        assert meson_data.get_benchmark().get_name() == 'null'
        assert meson_data.get_benchmark().get_priority() == 'null'
        assert meson_data.get_benchmark().get_suite() == 'null'
        assert meson_data.get_benchmark().get_timeout() == 'null'
        assert meson_data.get_benchmark().get_workdir() == 'null'

    def test_tests_as_null(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-38'])

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing test info
        assert meson_data.get_tests().get_environment() == 'null'
        assert meson_data.get_tests().get_is_parallel() == 'null'
        assert meson_data.get_tests().get_name() == 'null'
        assert meson_data.get_tests().get_priority() == 'null'
        assert meson_data.get_tests().get_suite() == 'null'
        assert meson_data.get_tests().get_timeout() == 'null'
        assert meson_data.get_tests().get_workdir() == 'null'

    def test_mesoninfo_as_null(self):
        prog = FakeProg()
        prog.set_sourcedir(test_case['case-39'])

        meson_data: MesonUiModule = MesonUiModule(prog)

        # Testing targets sources info
        assert meson_data.get_targets_sources().get_compiler() == 'null'
        assert meson_data.get_targets_sources().get_language() == 'null'
        assert meson_data.get_targets_sources().get_sources() == 'null'

        assert str(meson_data.get_mesoninfo().get_major_version()) == 'null'
        assert str(meson_data.get_mesoninfo().get_minor_version()) == 'null'
        assert str(meson_data.get_mesoninfo().get_full_version()) == 'null'
        assert str(meson_data.get_mesoninfo().get_patch_version()) == 'null'
