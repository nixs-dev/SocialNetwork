import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import views.Profile as Profile
from database.User import User
from database.Connection import Connection


conn = Connection()[1]
user_data = {'username': 'theAdm', 'display_name': 'ADM', 'profile_photo': 'NULL', 'password': 'santodeus123'}
User.insert(conn, user_data)