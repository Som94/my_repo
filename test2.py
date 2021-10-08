import mysql.connector

username=input("Enter user name :")
password=input("Enter user password :")
database=input("Enter database name :")
host=input("Enter host name :")
port=input("Enter port number :")
   
try: 
    conn=mysql.connector.connect(username=username,password=password,database=database,host=host,port=port)
    
    cursor=conn.cursor()
    
    model_name=input("Enter database model name :")
    cursor.execute('select * from {}'.format(model_name))
    data=cursor.fetchall()
    print(data)
    
except mysql.connector.DatabaseError as e:
    if e.errno==1146:
        #print("There is problem with sql :",e)
        print("Table doesn't exists")
        
    elif e.errno==1045:
        #print("There is problem with sql :",e)
        print("Provided Credentials are not proper")
