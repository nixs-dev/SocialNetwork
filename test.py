import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import views.Profile as Profile
from database.User import User
from database.Connection import Connection


conn = Connection()
photoData = open('C:\\Users\\x\\Pictures\\Eu\\pp66.jpg', 'rb').read()
User.updatePhoto(conn, photoData, 'theAdm')