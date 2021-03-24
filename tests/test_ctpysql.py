from mysql.connector import (connection)
from ctpysql import ctpysql

cnx = connection.MySQLConnection(user='roottest', password='test',
                                 host='127.0.0.1',
                                 database='testdb')

obj = ctpysql(cnx)

def test_insert():
    assert obj.insert('product', {'name': 'Salam'}) >= 1

def test_update():
    assert obj.update('product', 'id', '1', name='product') == 1
