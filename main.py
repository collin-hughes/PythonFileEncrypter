import passwordManager
import getpass
import utilities
import sys
import ui as UI
from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = UI.Controller()
    controller.ShowLogin()
    sys.exit(app.exec_())
    

main()