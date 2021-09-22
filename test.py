import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import views.Profile as Profile

app = QtWidgets.QApplication(sys.argv)
ProfileWindow = QtWidgets.QMainWindow()
ui = Profile.Ui_ProfileWindow()
ui.setupUi(ProfileWindow, '', '')
ProfileWindow.show()
sys.exit(app.exec_())