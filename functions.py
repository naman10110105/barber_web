#Connecting python to MySQL server

import mysql.connector
#import os
import hashlib

#os.system('sudo /etc/init.d/mysql start')

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='2111',
  auth_plugin='mysql_native_password',
  database='mydatabase'                                   #Connect to database with name "mydatabase"
)

mycursor = mydb.cursor()

def show_barber():
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'barbers' ORDER BY ORDINAL_POSITION")
    print(mycursor.fetchall())
    mycursor.execute("SELECT * FROM barbers")                #Select all the cloumns
    myresult = mycursor.fetchall()                            #Select all the rows
    return myresult

def add_barber(name,address):
    try:
        sql = "INSERT INTO barbers (name, address) VALUES (%s, %s)" 
        val = (name, address)
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        mycursor.execute("CREATE TABLE barbers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
        sql = "INSERT INTO barbers (name, address) VALUES (%s, %s)" 
        val = (name, address)
        mycursor.execute(sql, val)
        mydb.commit()

def delete_barber(id):
    sql = 'DELETE FROM barbers WHERE id = %s'
    mycursor.execute(sql, (id,))
    mydb.commit()

def update_barber(id,choice,update):
    sql = "UPDATE barbers SET "+ choice +" = %s WHERE id = %s"
    mycursor.execute(sql, (update,id))
    mydb.commit()

def location(city):
    sql= "SELECT name FROM barbers WHERE address = %s"
    mycursor.execute(sql, (city,))
    print(mycursor.fetchall())

def active_barber(id):
    sql= "SELECT Active FROM barbers WHERE id= %s"
    mycursor.execute(sql, (id,))
    status= mycursor.fetchone()
    if (status[0] == 'Y'):
        sql= "UPDATE barbers SET Active = 'N' WHERE id = %s"
        mycursor.execute(sql, (id,))
        mydb.commit()
    else:
        sql= "UPDATE barbers SET Active = 'Y' WHERE id = %s"
        mycursor.execute(sql, (id,))
        mydb.commit()

def login(username,password,stamp):
    sql= "SELECT * FROM login WHERE username= %s"       
    mycursor.execute(sql, (username,))        
    myresult = mycursor.fetchone()
    if (myresult!=None):
        hash_object = hashlib.sha1(str.encode(password))
        password = hash_object.hexdigest()
        sql= "INSERT INTO login (username, password, stamp) VALUES (%s, %s, %s)" 
        mycursor.execute(sql, (username,password,stamp))
        mydb.commit()
    else:
        print("Account does not exist")
        return myresult

def register(username, password, stamp):
    sql= "SELECT * FROM login WHERE username= %s"       
    mycursor.execute(sql, (username,))        
    myresult = mycursor.fetchone()
    if (myresult==None):
        hash_object = hashlib.sha1(str.encode(password))
        password = hash_object.hexdigest()
        sql= "INSERT INTO login (username, password, stamp) VALUES (%s, %s, %s)" 
        mycursor.execute(sql, (username,password,stamp))
        mydb.commit()
    else:
        print("Account already exist")
        return myresult

def insert_customer(name, location, username):
    sql= "SELECT id FROM login WHERE username= %s"
    mycursor.execute(sql, (username,))
    id= mycursor.fetchone()
    sql= "INSERT INTO customer (id, name, location) VALUES (%s, %s, %s)" 
    mycursor.execute(sql, (id[0], name, location))
    mydb.commit()