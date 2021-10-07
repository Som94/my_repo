import mysql.connector
from mysql.connector import errorcode

username=input("Enter User name :")
password=input("Enter the password :")
database=input("Enter the database name :")
host=input("Enter the hostname :")
port=input("Enter the port code :")

conn=mysql.connector.connect(user=username,password=password,database=database,host=host,port=port)

cursor = conn.cursor()

try:
  cursor.execute("DROP TABLE unknown")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_BAD_TABLE_ERROR:
    print(errorcode.ER_BAD_TABLE_ERROR)
    print("Table doesn't exists, Plz Create table unknown")
  