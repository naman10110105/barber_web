import mysql.connector

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='2111',
  auth_plugin='mysql_native_password',
  database='mydatabase'                                   #Connect to database with name "mydatabase"
)
mycursor = mydb.cursor()
#mycursor.execute("DELETE FROM login WHERE username = 'namanvashishth12@gmail.com'")
#mydb.commit()
mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'login' ORDER BY ORDINAL_POSITION")
print(mycursor.fetchall())
mycursor.execute("SELECT * FROM login")                #Select all the cloumns
myresult = mycursor.fetchall()
#print(myresult)
#if (myresult== None):
#  print("Yes")
#else:
#  print("No")
for x in myresult:
#for x in mycursor:
  print(x)