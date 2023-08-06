import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class Database():
    def __init__(self, config):
        self.hostaddr = config["hostaddr"]
        self.port = config["port"]
        self.dbname = config["dbname"]
        self.user = config["user"]
        self.passwd = config["passwd"]


    def conn(self):
        db = MySQLdb.connect(host=self.hostaddr,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.dbname,
                             use_unicode=True, charset="utf8mb4")
        return db

    def executequery(self, query):
        db = self.conn()
        cur = db.cursor()
        cur.execute(query)
        result = []
        for data in cur:
            innerdata = {}
            for i in range(len(data)):
                innerdata[cur.description[i][0]] = data[i]
            result.append(innerdata)
        cur.close()
        db.close()
        return result

