<div align=center>

  ![ctpysql](https://github.com/MahyarNV/cautious-pysql/blob/e740034826c6fa2ec46b61e9c67d1011e31c38b3/media/ctpysql.png)

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

mysql insert query:

`insert('table', {dictionary values})`

mysql table truncate query:

`truncate('table')`
