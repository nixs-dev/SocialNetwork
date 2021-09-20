import mysql.connector

class Post:

	def send(conn, username, title, body):
		cursor = conn.cursor()
		title = title.text()
		body = body.toPlainText()

		sql = 'INSERT INTO posts (author, title, body) VALUES("' + username + '", "'+ title + '", "' + body + '")';

		cursor.execute(sql)
		conn.commit()

	def getAll(conn):
		cursor = conn.cursor()

		sql = 'SELECT * FROM posts'

		cursor.execute(sql)
		
		posts = list(cursor.fetchall())
		changedPosts = [] 

		for p in posts:
			p = list(p)
			likes = len(Post.getLikes(conn, p[0]))
			p.append(likes)
			changedPosts.append(p)

		return changedPosts

	def getLikes(conn, post):
		cursor = conn.cursor()

		sql = 'SELECT * FROM likes WHERE postId = ' + str(post)

		cursor.execute(sql)

		return cursor.fetchall()

	def setLike(conn, post, user):
		cursor = conn.cursor()

		sql = 'INSERT INTO likes VALUES (' + str(post) + ', "' + user + '")';

		cursor.execute(sql);
		conn.commit();