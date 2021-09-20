import mysql.connector

class Connection:
	host = '127.0.0.1'
	port = 3306
	user = 'root'
	password = 'santodeus123'
	database='socialNetwork'

	def __new__(self):
		conn = mysql.connector.connect(
					host=self.host,
					port=self.port,
					user=self.user,
					password=self.password,
					database=self.database
				)
		
		return conn