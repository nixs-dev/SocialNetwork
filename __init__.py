import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from views.Login import Ui_LoginWindow
from views.Home import Ui_MainWindow
from database.Connection import Connection
from tools.Session import Session as session
from database.User import User as user


currentSession = session.readSession()
conn = Connection()

if currentSession != '':
	currentSession = currentSession.split('|')

	result = user.login(conn, currentSession[0], currentSession[1])

	if result[0] == 'Success':
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		ui = Ui_MainWindow()
		ui.setupUi(MainWindow, conn, result[1])
		MainWindow.show()
		sys.exit(app.exec_())
	else:
		print(result[0])
else:
	app = QtWidgets.QApplication(sys.argv)
	LoginWindow = QtWidgets.QMainWindow()
	ui = Ui_LoginWindow()
	ui.setupUi(LoginWindow, conn)
	LoginWindow.show()
	sys.exit(app.exec_())