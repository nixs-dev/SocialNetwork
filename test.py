import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import views.Profile as Profile
from database.User import User
from database.Connection import Connection


conn = Connection()
user = User.getUser(conn, 'theAdm')
print(user[0])