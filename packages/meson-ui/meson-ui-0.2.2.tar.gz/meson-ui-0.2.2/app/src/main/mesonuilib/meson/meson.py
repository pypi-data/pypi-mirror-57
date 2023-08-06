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
from PyQt5.QtCore import QProcess
from PyQt5.QtCore import QObject

from .minstall import MesonInstalle
from .msetup import MesonSetup
from .mdist import MesonDist
from .mtest import MesonTest
from ..ninja.ninja import Ninja
from ..utils.mesonconsts import MESON_INFO_SUPPORT
from ..utils.mesonconsts import MESON_DIST_SUPPORT
from subprocess import check_output


class Meson(QObject):
    '''
        This class is a wrapper for the Meson build system
    '''

    def __init__(self, context=None):
        super().__init__()
        self._context = context
        self._process: QProcess = QProcess(self)
        self._ninja = Ninja(context=self._context)
        self._minstall: MesonInstalle = MesonInstalle(self._context)
        self._msetup: MesonSetup = MesonSetup(self._context)
        self._mdist: MesonDist = MesonDist(self._context)
        self._mtest: MesonTest = MesonTest(self._context)
    # end of method

    def version(self):
        return check_output(['meson', '--version'], encoding='utf-8')

    def process(self) -> QProcess:
        return self._process

    def setup(self, args: list = []) -> None:
        self._msetup.run(args=args)
    # end of method

    def dist(self) -> None:
        if self.version() in MESON_DIST_SUPPORT:
            self._mdist.run()
        else:
            self._ninja.dist()
    # end of method

    def tests(self) -> None:
        if self.version() in MESON_INFO_SUPPORT:
            self._mtest.run()
        else:
            self._ninja.test()
    # end of method

    def build(self) -> None:
        self._ninja.build()
    # end of method

    def clean(self) -> None:
        self._ninja.clean()
    # end of method

    def install(self) -> None:
        if self.version() in MESON_INFO_SUPPORT:
            self._minstall.run()
        else:
            self._ninja.install()
    # end of method
