import functions

print("\n1. Login\n" "2. Register\n")
option= input("Please select an option: ")

if (option=="2"):
    username= input("Enter E-mail ID: ")
    password= input("Enter Password: ")
    stamp= "barber"
    myresult= functions.register(username,password,stamp)
    if (myresult== None):
        name= input("\n\n\nRegistered Successfully\n\n\nWelcome new barber \n\nEnter Name: ")
        location= input("Enter location: ")
        functions.insert_barber(name,location,username)

if (option=="1"):
    username= input("Enter E-mail ID: ")
    password= input("Enter Password: ")
    stamp= "barber"
    flag= functions.login(username,password,stamp)
    if (flag == 1):
        info= functions.account(username)
        print("Welcome back " + info[0])
        customers= input("Enter number of customers: ")
        workers= input("Enter number of workers: ")
        functions.barber_info(customers, workers, info[1])