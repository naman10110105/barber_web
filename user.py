import functions

print("\n1. Login\n" "2. Register\n")
option= input("Please select an option: ")

if (option=="2"):
    username= input("Enter E-mail ID: ")
    password= input("Enter Password: ")
    stamp= "customer"
    myresult= functions.register(username,password,stamp)
    if (myresult== None):
        name= input("\n\n\nRegistered Successfully\n\n\nWelcome new user \n\nEnter Name: ")
        location= input("Enter location: ")
        functions.insert_customer(name,location,username)

if (option=="1"):
    username= input("Enter E-mail ID: ")
    password= input("Enter Password: ")
    stamp= "customer"
    functions.login(username,password,stamp)
