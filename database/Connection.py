import mysql.connector


class Connection:
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = 'santodeus123'
    database = 'socialNetwork'

    def __new__(cls):
        try:
            conn = mysql.connector.connect(
                host=Connection.host,
                port=Connection.port,
                user=Connection.user,
                password=Connection.password,
                database=Connection.database
            )

            return [True, conn]
        except:
            return [False, "Impossível estabelecer a conexão com o Banco de dados"]
