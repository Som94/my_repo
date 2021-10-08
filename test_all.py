
import mysql.connector


username=input("Enter user name :")
password=input("Enter user password :")
database=input("Enter database name :")
host=input("Enter host name :")
port=input("Enter port number :")

try:

    conn=mysql.connector.connect(username=username,password=password,database=database,host=host,port=port)
    

    cursor = conn.cursor()
    model_name=input("Enter database model name :")
    sql = "select * from {}".format(model_name)
    cursor.execute(sql)
    data=cursor.fetchall()

    print(data)
 
    conn.close()

except mysql.connector.DataError as e:
    print("DataError")
    print(e)

except mysql.connector.InternalError as e:
    print("InternalError")
    print(e)

except mysql.connector.IntegrityError as e:
    print("IntegrityError")
    print(e)

except mysql.connector.OperationalError as e:
    print("OperationalError")
    print(e)

except mysql.connector.NotSupportedError as e:
    print("NotSupportedError")
    print(e)

except mysql.connector.ProgrammingError as e:
    print("ProgrammingError, Plz provide valid credentials ")
    print(e)

except mysql.connector.ProgrammingError as e:
    print("Unknown error occurred")
    print(e)
    
except mysql.connector.InterfaceError as e:
    print(e)