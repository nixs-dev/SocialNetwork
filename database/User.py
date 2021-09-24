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

	def update(conn, data, username):
		cursor = conn.cursor()
		sql = 'UPDATE users SET displayName = "' + data['displayName'] + '", _password = "' + data['password'] + '" WHERE username = "' + username + '";'

		cursor.execute(sql)
		conn.commit()

		return 'OK'