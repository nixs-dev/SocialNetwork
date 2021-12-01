import mysql.connector


class User:

	@staticmethod
	def login(conn, name, password):
		user = User.get_user(conn, name)

		if not user:
			return ['Usuário não encontrado']
		else:
			if user[0][3] == password:
				return ['Success', user[0]]
			else:
				return ['Senha incorreta']

	@staticmethod
	def get_user(conn, name):
		cursor = conn.cursor()
		sql = 'SELECT * FROM users WHERE username = "' + name +'"'
		cursor.execute(sql)

		user = cursor.fetchall()

		return user

	@staticmethod
	def update_photo(conn, photoData, user):
		cursor = conn.cursor()
		sql = 'UPDATE users SET photo = %s WHERE username = %s;'
		args = (photoData, user)
		cursor.execute(sql, args)
		conn.commit()

		return 'OK'

	@staticmethod
	def insert(conn, user_data):
		cursor = conn.cursor()
		sql = 'INSERT INTO users VALUES(%s, %s, %s, %s)'
		args = (user_data['username'], user_data['display_name'], user_data['profile_photo'], user_data['password'])

		try:
			cursor.execute(sql, args)
			conn.commit()
		except mysql.connector.errors.IntegrityError: # username already exists in database
			return 'DUPLICATE_KEY'

		return 'OK'

	@staticmethod
	def update(conn, data, username):
		cursor = conn.cursor()
		sql = 'UPDATE users SET displayName = %s, _password = %s WHERE username = %s;'
		args = (data['displayName'], data['password'], username)

		cursor.execute(sql, args)
		conn.commit()

		if data['profilePhoto'] != '':
			User.update_photo(conn, data['profilePhoto'], username)

		return 'OK'