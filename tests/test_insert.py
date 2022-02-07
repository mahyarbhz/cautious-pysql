from mysql.connector import (connection)
from ctpysql import ctpysql

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='ct_test')

obj = ctpysql(cnx)

def test_insert():
    assert obj.insert('employee', {'first_name': 'John', 'last_name': 'Doe'}) >= 1

def test_insert_int_input():
    assert obj.insert('employee', {'first_name': 123, 'last_name': 'Doe'}) >= 1

def test_insert_big_input():
    fn = 'Lorem ipsum dolor sit amet. Est maiores labore ut exercitationem culpa non internos Quis non excepturi iusto? Sit atque neque ab saepe consectetur sit natus architecto! Sit magni sunt ut sint explicabo et neque consequatur est maxime pariatur. Hic fugiat iure eos sint molestiae et voluptatem laudantium sed omnis dolores cum itaque incidunt quo iure ipsum et dolore quas. Sit omnis porro ut cumque aliquam nam adipisci sint.'
    assert obj.insert('employee', {'first_name': fn, 'last_name': 'Doe'}) >= 1

def test_end_truncate():
    assert obj.truncate('employee') == 1