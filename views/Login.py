# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from database.User import User as user
import views.Home as Home
import views.SignUp as SignUp
from tools.Session import Session as session


class Ui_LoginWindow(object):
    dbConn = None

    def login(self, LoginWindow, event):
        result = user.login(self.dbConn, self.username.text(), self.password.text())

        if result[0] != 'Success':
            self.error.setText(result[0])
        else:
            session.saveSession(result[1][0] + '|' + result[1][3])
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Home.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow, self.dbConn, result[1])
            self.MainWindow.show()
            LoginWindow.close()

    def go_to_sign_up(self, LoginWindow, event):
        self.window = QtWidgets.QMainWindow()
        self.signup_ui = SignUp.Ui_RegisterWindow()
        self.signup_ui.setup_ui(self.window, self.dbConn)
        self.window.show()
        LoginWindow.close()


    def additional_config(self, LoginWindow):
        LoginWindow.setFixedSize(1024, 768)
        self.signUp.mousePressEvent = partial(self.go_to_sign_up, LoginWindow)
        self.pushButton.clicked.connect(partial(self.login, LoginWindow))

    def setupUi(self, LoginWindow, conn):

        self.dbConn = conn

        #################################################### QT DESIGNER ###############################################

        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setWindowModality(QtCore.Qt.NonModal)
        LoginWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        LoginWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("assets/authBackground.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.container = QtWidgets.QFrame(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(330, 280, 411, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.container.setPalette(palette)
        self.container.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.label_username = QtWidgets.QLabel(self.container)
        self.label_username.setGeometry(QtCore.QRect(50, 10, 101, 101))
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.container)
        self.label_password.setGeometry(QtCore.QRect(50, 70, 101, 101))
        self.label_password.setObjectName("label_password")
        self.username = QtWidgets.QLineEdit(self.container)
        self.username.setGeometry(QtCore.QRect(160, 50, 220, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.container)
        self.password.setGeometry(QtCore.QRect(160, 110, 220, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.container)
        self.pushButton.setGeometry(QtCore.QRect(304, 232, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.error = QtWidgets.QLabel(self.container)
        self.error.setGeometry(QtCore.QRect(50, 160, 251, 16))
        self.error.setStyleSheet("color: rgb(255, 0, 0);")
        self.error.setText("")
        self.error.setObjectName("error")
        self.signUp = QtWidgets.QLabel(self.container)
        self.signUp.setGeometry(QtCore.QRect(240, 210, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.signUp.setFont(font)
        self.signUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signUp.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.signUp.setObjectName("signUp")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(330, 170, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(6, 52, 113);")
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        LoginWindow.setCentralWidget(self.centralwidget)




        #################################################################################################################

        self.additional_config(LoginWindow)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.label_username.setText(_translate("LoginWindow", "Nome de usuário:"))
        self.label_password.setText(_translate("LoginWindow", "Senha:"))
        self.pushButton.setText(_translate("LoginWindow", "👉🏻"))
        self.signUp.setText(_translate("LoginWindow", "Create a account"))
        self.title.setText(_translate("LoginWindow", "Login"))
