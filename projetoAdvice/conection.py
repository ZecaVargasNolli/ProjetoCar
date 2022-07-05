import psycopg2 as db

class Config:
    def __init__(self):
        self.config = {
            "postgress": {
                "user": "postgres",
                "password": "postgres",
                "host": "172.28.1.4",
                "database": "postgres"
            }
        }

#Classe de coneçaão do sistema
class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgress"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("ERRO AO CRIAR")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.getConnection.close()

    @property
    def getConnection(self):
        return self.conn

    @property
    def getCursor(self):
        return self.cur

    def commit(self):
        self.getConnection.commit()

    def fetchall(self):
        return self.getCursor.fetchall()

    def execute(self, sql, params=None):
        self.getCursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.getCursor.execute(sql, params or ())
        return self.fetchall()