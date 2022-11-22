from controller.controller_dao import Controller
import sys
from PyQt5 import QtWidgets
from view.view_of_windows import View_of_windows


class View_class:
    def __init__(self, controller: Controller):
        self.controller = controller

    def start_window(self, controller: Controller):
        pass

    def build(self):
        APP = QtWidgets.QApplication(sys.argv)
        w = View_of_windows(self.controller).ChooseWindow()
        w.show()
        sys.exit(APP.exec_())
