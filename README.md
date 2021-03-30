<div align=center>

  ![ctpysql](https://github.com/MahyarNV/cautious-pysql/blob/e740034826c6fa2ec46b61e9c67d1011e31c38b3/media/ctpysql.png)

</div>
<div align="center">
<a href="https://discord.com/invite/aHXATxBuAh"><img src='https://img.shields.io/badge/Discord-Server-868fff?logo=discord' alt='Discord Server' /></a>
<a href="https://twitter.com/CautiousNV"><img src='https://img.shields.io/badge/Twitter-Account-blue?logo=twitter' alt='Twitter Account' /></a>
<a href="https://github.com/MahyarNV/cautious-pysql"><img src='https://img.shields.io/badge/Build-Passing-success' alt='Build Passing' /></a>
</div>

# cautious-pysql
CTpysql helps you to code mysql queries as fast as possible 🚄🔥

## Usage
### Installation
Use `pip install ctpysql` to install the *ctpysql* and it's dependencies on your pc (or venv).

import module with:

`from ctpysql import ctpysql`

to use it in your project.
### How it works?
You may import mysql.connector to work with ctpysql, just use:

`from mysql.connector import (connection, Error)`

and make a connection like this:

`cnx = connection.MySQLConnection(user='root', password='password', host='127.0.0.1', database='db')`

then make an object from *ctpysql* class using this connection:

`obj = ctpysql(cnx)`

after these steps you are able to use this library correctly, for example, insert query using dictionary values:

`obj.insert('users', {'username': 'user1', 'password': 'password1'})`

## Supported queries
Supported queries at this version (they will be more soon):
<hr>

### Insert
Last rowid inserted return

`insert('table', {dictionary values})`
<hr>
Truncate:

`truncate('table')`
<hr>

### Select
Selected row(s) return

`fetch('table', 'case [all or one]', 'type [dic or None]', **data)`

Example:
`fetch('users', 'one', None, id=3)`
<hr>

#### Select all
Selected row(s) return

`fetchall('table', 'type [dic or None]')`

Example 1:
`fetchall('products', None)`

Example 2:
`fetchall('products', 'dic')`

<hr>

### Update
Affected rows count return

`update('table', 'condition column name', 'condition column value', **data)`

Example:
`update('users', 'username', usernameVar, password=123, email=a@a.com)`

<hr>

### Delete
Deleted rows count return

`delete('table', 'condition column name', 'condition value')`
<hr>

### Drop
"Success" or error return

`drop('case', 'name')`

Example:
`drop('table', 'product')`

Example2:
`drop('view', '[mysql queries]')`
<hr>

### Order
Fetched items return

`order('table', **data(column1="order like ASC", column2="order like DESC"))`

Example:
`order('products', name="ASC", id="DESC")`
<hr>

### Create table
"Success" or error return

`create_table('table name', **data)`

Example:
`create_table('users', id="INT AUTO_INCREMENT PRIMARY KEY", name="VARCHAR(255)")`
<hr>

### Between
Fetched rows return

`between('table name', 'type [dic or None]', 'condition column', 'first parameter', 'second parameter')`

Example:
`between('products', None, 'id', 1, 4)`
<hr>

### Advanced Commit
Row count return
```
query = "INSER INTO table (column) VALUES ('value')"
advanced_commit(query)
```

Example:
```python
query = "INSER INTO products (name) VALUES ('Laptop')"
advanced_commit(query)
```
<hr>

## Don't forget!
Don't forget this is a class and you should call this functions from an object of class. A full example here:

```python
from mysql.connector import (connection, Error)
from ctpysql import ctpysql

connection = connection.MySQLConnection(user='root', password='password', host='127.0.0.1', database='testdb')
object = ctpysql(cnx)
object.insert('products', {'name': 'Laptop', 'brand': 'Asus'})
```
