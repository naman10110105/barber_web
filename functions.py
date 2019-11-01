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
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'barber' ORDER BY ORDINAL_POSITION")
    print(mycursor.fetchall())
    mycursor.execute("SELECT * FROM barber")                #Select all the cloumns
    myresult = mycursor.fetchall()                            #Select all the rows
    return myresult

def add_barber(name,address):
    sql = "INSERT INTO barber (name, address) VALUES (%s, %s)" 
    val = (name, address)
    mycursor.execute(sql, val)
    mydb.commit()
    
def delete_barber(id):
    sql = 'DELETE FROM barber WHERE id = %s'
    mycursor.execute(sql, (id,))
    mydb.commit()
    sql = 'DELETE FROM login WHERE id = %s'
    mycursor.execute(sql, (id,))
    mydb.commit()

def update_barber(id,choice,update):
    sql = "UPDATE barber SET "+ choice +" = %s WHERE id = %s"
    mycursor.execute(sql, (update,id))
    mydb.commit()

def location(city):
    sql= "SELECT name FROM barber WHERE address = %s"
    mycursor.execute(sql, (city,))
    print(mycursor.fetchall())

def active_barber(id):
    sql= "SELECT Active FROM barber WHERE id= %s"
    mycursor.execute(sql, (id,))
    status= mycursor.fetchone()
    if (status[0] == 'Y'):
        sql= "UPDATE barber SET Active = 'N' WHERE id = %s"
        mycursor.execute(sql, (id,))
        mydb.commit()
    else:
        sql= "UPDATE barber SET Active = 'Y' WHERE id = %s"
        mycursor.execute(sql, (id,))
        mydb.commit()

def login(username,password,stamp):
    sql= "SELECT password FROM login WHERE username= %s AND stamp= %s"       
    mycursor.execute(sql, (username,stamp))        
    myresult = mycursor.fetchone()
    if (myresult!=None):
        hash_object = hashlib.sha1(str.encode(password))
        password = hash_object.hexdigest()
        sql= "SELECT password FROM login WHERE username= %s" 
        mycursor.execute(sql, (username,))
        correct_password= mycursor.fetchone()
        if (password == correct_password[0]):
            print("Login Successful")
            flag=1
        else:
            print("Incorrect password")
            flag=0
        return flag
    else:
        print("Barber account does not exist")

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
        print("Account already exist as a "+ stamp)
        return myresult

def insert_customer(name, location, username):
    sql= "SELECT id FROM login WHERE username= %s"
    mycursor.execute(sql, (username,))
    id= mycursor.fetchone()
    sql= "INSERT INTO customer (id, name, location) VALUES (%s, %s, %s)" 
    mycursor.execute(sql, (id[0], name, location))
    mydb.commit()

def insert_barber(name, location, username):
    sql= "SELECT id FROM login WHERE username= %s"
    mycursor.execute(sql, (username,))
    id= mycursor.fetchone()
    sql= "INSERT INTO barber (id, name, location) VALUES (%s, %s, %s)" 
    mycursor.execute(sql, (id[0], name, location))
    mydb.commit()

def account(username):
    sql= "SELECT stamp FROM login WHERE username= %s"
    mycursor.execute(sql, (username,))
    stamp= mycursor.fetchone()
    sql= "SELECT id FROM login WHERE username= %s"
    mycursor.execute(sql, (username,))
    id= mycursor.fetchone()
    if (stamp[0]== 'customer'):
        sql= "SELECT name , location FROM customer WHERE id= %s"
        mycursor.execute(sql, (id[0],))
        info= mycursor.fetchone()
        return info
    if (stamp[0]== 'barber'):
        sql= "SELECT name FROM barber WHERE id= %s"
        mycursor.execute(sql, (id[0],))
        info= mycursor.fetchone()
        return info[0], id[0]

def barber_info(workers, customers, id):
    sql= "UPDATE barber SET workers = %s, customers = %s WHERE id = %s"
    mycursor.execute(sql, (workers,customers,id))
    mydb.commit()

def customer_barber(location):
    print("Name     Workers  Customers")
    sql= "SELECT name, customers, workers FROM barber WHERE location= %s AND active= 'Y'"
    mycursor.execute(sql, (location,))
    myresult= mycursor.fetchall()
    for x in myresult:
        print(x)
