import mysql.connector

class User:

	def login(conn, name, password):
		user = User.getUser(conn, name)

		if user == []:
			return ['Usuário não encontrado']
		else:
			if user[0][3] == password:
				return ['Success', user[0]]
			else:
				return ['Senha incorreta']

	def getUser(conn, name):
		cursor = conn.cursor()
		sql = 'SELECT * FROM users WHERE username = "' + name +'"'
		cursor.execute(sql)

		user = cursor.fetchall()

		return user

	def updatePhoto(conn, photoData, user):
		cursor = conn.cursor()
		sql = 'UPDATE users SET photo = %s WHERE username = %s;'
		args = (photoData, user)
		cursor.execute(sql, args)
		conn.commit()

		return 'OK'

	def update(conn, data, username):
		cursor = conn.cursor()
		sql = 'UPDATE users SET displayName = %s, _password = %s WHERE username = %s;'
		args = (data['displayName'], data['password'], username)

		cursor.execute(sql, args)
		conn.commit()

		if data['profilePhoto'] != '':
			User.updatePhoto(conn, data['profilePhoto'], username)

		return 'OK'