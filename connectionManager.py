import mysql.connector


class connectionManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão estabelecida com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            self.connection = None

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Erro ao executar a consulta: {err}")
            return []

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão fechada com sucesso!")
