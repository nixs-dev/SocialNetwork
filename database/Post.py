import mysql.connector

class Post:

	def send(conn, username, title, body):
		cursor = conn.cursor()
		title = title.text()
		body = body.toPlainText()

		sql = 'INSERT INTO posts VALUES("'+ title + '", "' + body + '", "' + username + '")'

		cursor.execute(sql)
		conn.commit()

	def getAll(conn):
		cursor = conn.cursor()

		sql = 'SELECT * FROM posts'

		cursor.execute(sql)
		
		return cursor.fetchall() 