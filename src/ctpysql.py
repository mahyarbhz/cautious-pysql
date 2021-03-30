from mysql.connector import (Error)

class ctpysql:
    def __init__(self, conn):
        self.conn = conn
        self.Error = Error

    def truncate (self, table_name):
        sql = "truncate {0}".format(table_name)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            freturn = "Success"

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def insert (self, table_name, dic):
        # dic: insert values with {'dic': 'dictionary'}
        columns = ', '.join("`" + str(i).replace('/', '_') + "`" for i in dic.keys())
        values = ', '.join("'" + str(i).replace('/', '_') + "'" for i in dic.values())
        sql = "INSERT INTO {0} ({1}) VALUES ({2})".format(table_name, columns, values)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            freturn = cursor.lastrowid

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def fetch(self, table_name, case, type, **data):
        # case: all or one
        # type: dic|dictionary or ... (everything else fetch it simply)
        # data: kwargs condition data like: id=3
        sql = "SELECT * FROM {0} ".format(table_name)
        for key, value in data.items():
            i = list(data.keys()).index(key)
            if i == 0:
                sql += "WHERE "

            sql += "{0}={1}".format(key, value)
            if i < len(data.items())-1:
                sql += " AND "

        if type == 'dic' or type == 'dictionary':
            cursor = self.conn.cursor(dictionary=True)

        else:
            cursor = self.conn.cursor()

        try:
            cursor.execute(sql)
            if case == 'all':
                freturn = cursor.fetchall()

            elif case == 'one':
                freturn = cursor.fetchone()

            else:
                freturn = "Incorrect parameter"

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def fetchall(self, table_name, type=None):
        # type: dic|dictionary or ... (everything else fetch it simply)
        sql = "SELECT * FROM {0}".format(table_name)
        if type == 'dic' or type == 'dictionary':
            cursor = self.conn.cursor(dictionary=True)

        else:
            cursor = self.conn.cursor()

        try:
            cursor.execute(sql)
            freturn = cursor.fetchall()

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def update(self, table_name, condition=None, condition_value=None, **data):
        # condition: your condition for update
        # condition_value: your condition value for condition
        # data: kwargs data tp update, like data='data', username='newUsername'
        sql = "UPDATE {0} SET ".format(table_name)
        for key, value in data.items():
            if type(value) is str:
                sql += "{0} = '{1}'".format(key, value)

            else:
                sql += "{0} = {1}".format(key, value)

            i = list(data.keys()).index(key)
            if i < len(data.items())-1:
                sql += ", "

        if condition:
            if type(condition_value) is str:
                sql += " WHERE {0} = '{1}'".format(condition, condition_value)

            else:
                sql += " WHERE {0} = {1}".format(condition, condition_value)

        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            freturn = cursor.rowcount

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def delete(self, table_name, condition, condition_value):
        # condition: your condition for update
        # condition_value: your condition value for condition
        sql = "DELETE FROM {0} WHERE {1} = {2} ".format(table_name, condition, condition_value)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            freturn = cursor.rowcount

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def drop(self, case, name):
        # case: can define what we want to drop, like: 'table' or 'veiw'
        # name: name of our case
        sql = "DROP {0} {1}".format(case, name)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            freturn = "Success"

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def order(self, table_name, **data):
        # data: kwargs data like: name="ASC", id="DESC"
        sql = "SELECT * FROM {0} ORDER BY ".format(table_name)
        for key, value in data.items():
            sql += "{0} {1}".format(key, value)

            i = list(data.keys()).index(key)
            if i < len(data.items())-1:
                sql += ", "

        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            freturn = cursor.fetchall()

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def create_table(self, table_name, **data):
        # data: kwargs data like: id="INT AUTO_INCREMENT PRIMARY KEY"
        sql = "CREATE TABLE {0} {1}".format(table_name, "(")
        for key, value in data.items():
            sql += "{0} {1}".format(key, value)

            i = list(data.keys()).index(key)
            if i < len(data.items())-1:
                sql += ", "

            elif i == len(data.items())-1:
                sql += ")"

        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            freturn = "Success"

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def between(self, table_name, type, condition_column, firstpram, secondpram):
        # type: dic|dictionary or ... (everything else fetch it simply)
        sql = "SELECT * FROM {0} WHERE {1} BETWEEN %s AND %s".format(table_name, condition_column)
        data = (firstpram, secondpram)
        if type == 'dic' or type == 'dictionary':
            cursor = self.conn.cursor(dictionary=True)

        else:
            cursor = self.conn.cursor()

        try:
            cursor.execute(sql, data)
            freturn = cursor.fetchall()

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn

    def advanced_commit(self, query):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            self.conn.commit()
            freturn = cursor.rowcount

        except Error as e:
            freturn = e

        finally:
            cursor.close()
            return freturn
