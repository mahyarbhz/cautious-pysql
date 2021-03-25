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

### Usage
#### Installation
Use `pip install ctpysql` to install the *ctpysql* and it's dependencies on your pc (or venv).

import module with:

`from ctpysql import ctpysql`

to use it in your project.
#### How it works?
You may import mysql.connector to work with ctpysql, just use:

`from mysql.connector import (connection, Error)`

and make a connection like this:

`cnx = connection.MySQLConnection(user='root', password='password, host='127.0.0.1', database='db')`

then make an object from *ctpysql* class using this connection:

`obj = ctpysql(cnx)`

after these steps you are able to use this library correctly, for example, insert query using dictionary values:

`obj.insert('users', {'username': 'user1', 'password': 'password1'})`

### Supported queries
supported queries at this version (they will be more soon):
<hr>
Mysql insert query (rowid return):

`insert('table', {dictionary values})`
<hr>
Mysql table truncate query:

`truncate('table')`
<hr>
Mysql select query (object return):

`fetch('table', 'case [all or one]', 'type [dic or None]', {dictionary values (for select)})`
<hr>
Mysql update query (affected rows count return):

`update('table', 'condition column name', 'condition column value', **data)`

Example:
```update('users', 'username', usernameVar, password=123, email=a@a.com)```
<hr>
Mysql delete query (deleted rows count return):

`delete('table', 'condition column name', 'condition value')`
<hr>
Mysql drop query ("Success" or error return):

`delete('table', 'condition column name', 'condition value')`
<hr>
Mysql order by query (fetched items return):

`order('table', **data(column1="order like ASC", column2="order like DESC"))`

Example:
```order('products', name="ASC", id="DESC")```
