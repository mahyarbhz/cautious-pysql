from mysql.connector import (Error)

class ctpysql:
    def __init__(self, conn):
        self.conn = conn
        self.Error = Error

    def truncate (self, table):
        sql = "truncate {0}".format(table)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            return "Success"

        except Error as e:
            return e


    def insert (self, table, dic):
        columns = ', '.join("`" + str(i).replace('/', '_') + "`" for i in dic.keys())
        values = ', '.join("'" + str(i).replace('/', '_') + "'" for i in dic.values())
        sql = "INSERT INTO {0} ({1}) VALUES ({2})".format(table, columns, values)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return cursor.lastrowid
            cursor.close()

        except Error as e:
            return e

    def fetch(self, table, case, type, dic):
        condition = ""
        for i in dic:
            if condition != "":
                condition += " AND {0} = {1}".format(i, dic[i])

            else:
                condition += "{0} = {1}".format(i, dic[i])

        sql = "SELECT * FROM {0} WHERE {1}".format(table, condition)
        try:
            if type == 'dic' or type == 'dictionary':
                cursor = self.conn.cursor(dictionary=True)

            else:
                cursor = self.conn.cursor()
            cursor.execute(sql)
            if case == 'all':
                row = cursor.fetchall()

            elif case == 'one':
                row = cursor.fetchone()
            cursor.close()
            return row

        except Error as e:
            return e

    def update(self, table, condition, condition_value, **data):
        sql = "UPDATE {0} SET ".format(table)
        i = 0
        for key, value in data.items():
            sql += "{0} = {1}".format(key, value)
            if i < len(data.items())-1:
                sql += ", "
            i += 1

        sql += " WHERE {0} = {1}".format(condition, condition_value)

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return cursor.rowcount
            cursor.close()

        except Error as e:
            return e

    def delete(self, table, condition, condition_value):
        sql = "DELETE FROM {0} WHERE {1} = {2} ".format(table, condition, condition_value)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return cursor.rowcount
            cursor.close()

        except Error as e:
            return e
