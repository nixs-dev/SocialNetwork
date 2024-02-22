import mysql.connector


class Post:

	@staticmethod
	def send(conn, username, title, body):
		cursor = conn.cursor()

		sql = 'INSERT INTO posts (author, title, body) VALUES("' + username + '", "'+ title + '", "' + body + '")'

		cursor.execute(sql)
		conn.commit()

		return 'OK'

	@staticmethod
	def get_all(conn):
		cursor = conn.cursor()

		sql = 'SELECT * FROM posts'

		cursor.execute(sql)
		
		posts = list(cursor.fetchall())
		changed_posts = []

		for p in posts:
			p = list(p)
			p[1] = Post.get_author(conn, p[1])
			likes = len(Post.get_likes(conn, p[0]))
			comments = len(Post.get_comments(conn, p[0]))
			p.append(likes)
			p.append(comments)
			changed_posts.append(p)

		return changed_posts

	@staticmethod
	def get_author(conn, username):
		cursor = conn.cursor()
		sql = 'SELECT * FROM users WHERE username = "' + username + '"'

		cursor.execute(sql)

		return cursor.fetchall()[0]

	@staticmethod
	def get_likes(conn, post):
		cursor = conn.cursor()

		sql = 'SELECT * FROM likes WHERE postId = ' + str(post)

		cursor.execute(sql)

		return cursor.fetchall()

	@staticmethod
	def send_like(conn, post, user):
		cursor = conn.cursor()

		sql = 'INSERT INTO likes VALUES (' + str(post) + ', "' + user + '")'

		cursor.execute(sql);
		conn.commit()

	@staticmethod
	def get_comments(conn, post):
		cursor = conn.cursor()

		sql = 'SELECT * FROM comments WHERE postId = ' + str(post)

		cursor.execute(sql)

		return cursor.fetchall()

	@staticmethod
	def send_comment(conn, post, user, text):
		cursor = conn.cursor()

		sql = 'INSERT INTO comments VALUES (' + str(post) + ', "' + user + '", "' + text + '")'

		cursor.execute(sql)
		conn.commit()
