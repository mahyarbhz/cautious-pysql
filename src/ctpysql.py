class ctpysql:
    def __init__(self, conn):
        self.conn = conn

    def truncate (self, table):
        sql = "truncate {0}".format(table)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            return self.conn.commit()

        except Error as e:
            return e

        cursor.close()

    def insert (self, table, dic):
        columns = ', '.join("`" + str(i).replace('/', '_') + "`" for i in dic.keys())
        values = ', '.join("'" + str(i).replace('/', '_') + "'" for i in dic.values())
        sql = "INSERT INTO {0} ({1}) VALUES ({2})".format(table, columns, values)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            return self.conn.commit()

        except Error as e:
            return e

        cursor.close()
