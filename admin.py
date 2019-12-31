#admin module 
import functions
a = 50
b = a+1
print (b)
while True:

    print("\n1. Show All\n" "2. Add Barber\n" "3. Delete Barber\n" "4. Update Barber\n" "5. Set Active/Inactive\n")
    option= input("Please select an option: ")

    if (option=="1"):
        ans = functions.show_barber()
        for x in ans:
            print(x)
    elif (option=="2"):
        username= input("Enter E-mail ID: ")
        password= input("Enter Password: ")
        stamp= "barber"
        myresult= functions.register(username,password,stamp)
        if (myresult== None):
            name= input("\n\n\nRegistered Successfully\n\n\nWelcome new barber \n\nEnter Name: ")
            location= input("Enter location: ")
            functions.insert_barber(name,location,username)
    elif (option=="3"):
        ans = functions.show_barber()
        for x in ans:
            print(x)
        id= input("Enter ID: ")
        functions.delete_barber(id)
        print("Record deleted successfully")
    elif (option=="4"):
        ans = functions.show_barber()
        for x in ans:
            print(x)
        id= input("Enter ID: ")
        choice= input("Enter choice (column name): ")
        update= input("Enter updated " + choice + ": ")
        functions.update_barber(id, choice, update)
    elif (option=="5"):
        ans = functions.show_barber()
        for x in ans:
            print(x)
        id= input("Enter ID to change Active status: ")
        functions.active_barber(id)
        print("Active status changed successfully")
        