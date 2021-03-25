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
        # dic: insert values with {'dic': 'dictionary'}
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
        # case: all or one
        # type: dic|dictionary or ... (everything else fetch it simply)
        # dic: condition values with {'dic': 'dictionary'}
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

    def update(self, table, condition=None, condition_value=None, **data):
        # condition: your condition for update
        # condition_value: your condition value for condition
        # data: kwargs data tp update, like data='data', username='newUsername'
        sql = "UPDATE {0} SET ".format(table)
        i = 0
        for key, value in data.items():
            if type(value) is str:
                sql += "{0} = '{1}'".format(key, value)

            else:
                sql += "{0} = {1}".format(key, value)

            if i < len(data.items())-1:
                sql += ", "
            i += 1

        if condition:
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
        # condition: your condition for update
        # condition_value: your condition value for condition
        sql = "DELETE FROM {0} WHERE {1} = {2} ".format(table, condition, condition_value)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return cursor.rowcount
            cursor.close()

        except Error as e:
            return e

    def drop(self, case, name):
        sql = "DROP {0} {1}".format(case, name)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            return "Success"

        except Error as e:
            return e
