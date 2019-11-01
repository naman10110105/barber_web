import mysql.connector

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='2111',
  auth_plugin='mysql_native_password',
  database='mydatabase'                                   #Connect to database with name "mydatabase"
)
mycursor = mydb.cursor()
#mycursor.execute("DELETE FROM barber")
#mydb.commit()
#mycursor.execute("SHOW TABLES")
#mycursor.execute("DELETE FROM login")
a=5
b=2
c=14
sql= "UPDATE barber SET workers= %s, customers= %s WHERE id= %s"
mycursor.execute(sql, (a,b,c))
mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'barber' ORDER BY ORDINAL_POSITION")
print(mycursor.fetchall())
mycursor.execute("SELECT * FROM barber")                #Select all the cloumns
myresult = mycursor.fetchall()
#print(myresult)
#if (myresult== None):
#  print("Yes")
#else:
#  print("No")
for x in myresult:
#for x in mycursor:
  print(x)