import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root',password='root', database='test')
cursor = cnx.cursor()
#cursor.execute("DROP TABLE unknown")


try:
  cursor.execute("DROP TABLE unknown")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_BAD_TABLE_ERROR:
    print(errorcode.ER_BAD_TABLE_ERROR)
    print("Table doesn't exists, Plz Create table unknown")
  