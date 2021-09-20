import mysql.connector

class User:

	def login(conn, name, password):
		user = User.getUser(conn, name)

		if user == []:
			return ['Usuário não encontrado']
		else:
			if user[0][1] == password:
				return ['Success', user[0]]
			else:
				return ['Senha incorreta']

	def getUser(conn, name):
		cursor = conn.cursor()
		sql = 'SELECT * FROM users WHERE username = "' + name +'"'
		cursor.execute(sql)

		user = cursor.fetchall()

		return user