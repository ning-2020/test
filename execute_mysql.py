import pymysql
data_info = {
    "host" : "127.0.0.1",
    "user" : "root",
    "password" : "root",
    "port" : 3306
}
class DbConnect():
    def __init__(self,db_info,database=""):
        self.db_info = db_info
        self.db = pymysql.connect(database=database,
                                cursorclass=pymysql.cursors.DictCursor,
                                **db_info)
        self.cursor = self.db.connect()
    def select_sql(self,sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

if __name__ == '__main__':
    db = DbConnect(db_info=data_info,database="njb")
    print("数据库连接成功%s" %db)
    sql = "select * from user_info"
    results = db.select_sql(sql)
    print(results)

