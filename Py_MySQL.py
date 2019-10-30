#Connecting python to MySQL server

import mysql.connector

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='2111',
  auth_plugin='mysql_native_password',
  database='mydatabase'                                   #Connect to database with name "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")           #Create Database with name "mydatabase"

#mycursor.execute("SHOW DATABASES")                       #Shows all the databases

#Print name of Databases

#for x in mycursor:
#  print(x)

#Create a new table with Primary Key

#mycursor.execute("CREATE TABLE barbers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#Alter the existing table's columns

#mycursor.execute("ALTER TABLE barbers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#Show Table names

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#  print(x)

#To insert single data into the table

#sql = "INSERT INTO barbers (name, address) VALUES (%s, %s)"

#val = ("John", "Highway 21")
#mycursor.execute(sql, val)

#To insert multiple datas into the table

# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)

#Command to commit changes to the database

#val= input("Enter field name: ")
#sql = "UPDATE barbers SET" + val +"= 'pune' WHERE id = '15'"

#mycursor.execute("ALTER TABLE barbers ADD active varchar(255)")

#To see data from a table

#mycursor.execute("SELECT * FROM barbers")                #Select all the cloumns
#mycursor.execute("SELECT name FROM barbers")
#mycursor.execute("SHOW COLUMNS FROM barbers")
#mycursor.execute("ALTER TABLE barbers ALTER Active SET DEFAULT 'N'")            #Set default value of a column
#mycursor.execute("DELETE FROM barbers WHERE name = 'Naman'")
mydb.commit()
#print (mycursor.fetchall())
#mycursor.execute("SELECT address FROM barbers")              #Select "name" column
#mycursor.execute("SELECT * FROM barbers WHERE address LIKE '%way%'")                #Select a particular field with matching characters
#mycursor.execute("SELECT * FROM barbers ORDER BY name")                     #Sort name in ascending order and for descending order add "DESC"
#mycursor.execute("DROP TABLE barbers")                                       #Deletes the table
#mycursor.execute("DROP TABLE IF EXISTS barbers")                                       #Deletes the table if it exists
#myresult = mycursor.fetchall()                            #Select all the rows
#myresult = mycursor.fetchone()                             #Select first row
#for x in myresult:
#  print(x)

