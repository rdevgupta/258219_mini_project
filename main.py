import os
#function for adding data of the employee to the file
def AddData():
    print("Enter the Following details about the employee please: ")
    sfid = input("Enter the SFID of Employee: \n")
    name = input("Enter the name of Employee: \n")
    email = input("Enter email id: \n")
    designation = input("Position in the company: \n")
    phno = input("Enter Phone number: \n")
    #main data file containing all the data of employee
    file = open("EmployeeData.txt", "at")
    file.write(sfid+"   "+name+"     "+email+"             "+designation+"             "+phno+"\n")
    file.close()
    print("Data added successfully!....")

#function to display the data from the file
def ViewData():
    print("SFID     NAME                EMAIL                      DESIGNATION          PHNO")
    file = open("EmployeeData.txt", 'r')
    content = file.read()
    print(content)
    file.close()

#search the employee using his/her sfid
def SearchEmployee(sfid):
    file = open("EmployeeData.txt", "r")
    content = file.readlines()
    flag = 0
    for line in content:
        if line[0:6] == sfid:
            flag = 1
            print("SFID     NAME                EMAIL                      DESIGNATION          PHNO")
            print(line)
    if flag == 0:
        print("ERROR: Employee not Found with the entered sfid!")
    file.close()

#to delete particular employee
def DeleteEmployee(sfid):
    file = open("EmployeeData.txt", "r")
    content = file.readlines()
    file.close()
    
    new_file = open("EmployeeData.txt","w")
    for line in content:
        if line[0:6] != sfid:
            new_file.write(line)
    new_file.close()

#delete the entire data file permenantly
def DeleteData():
    print("Data is permenantly deleted...")
    if os.path.exists("EmployeeData.txt"):
        os.remove("EmployeeData.txt")
    else:
        print("The file does not exist")
#main driver code or menu of the system

print('''
********** Welcome to L&T Employee Management Service **********

******************************MENU******************************

                          1. ADD DATA    

                          2. VIEW DATA

                          3. SEARCH EMPLOYEE  

                          4. DELETE DATA OF AN EMPLOYEE   

                          5. DELETE ENTIRE DATA

                          6. EXIT                          ''')

choice = int(input("What you want to do with database, make a choice: "))

while choice != 0:
    if choice == 1:
        while(choice == 1):
            AddData()
            choice = int(input("Want to add Another Entry: 1 for yes and 0 for no\n"))
    elif choice == 2:
        print("Here is the data of all the employess: ")
        ViewData()
    elif choice == 3:
        print("Enter the SFID of the employee You want to search: ")
        sfid_str = input()
        SearchEmployee(sfid_str)
    elif choice == 4:
        # delete entry of employee
        print("Enter the SFID of the employee whose data to be deleted")
        sfid_del = input()
        DeleteEmployee(sfid_del)
        print("Data deleted Successfully!....\n")
    elif choice == 5:
        print("Entire data will be lost forever.... are you sure to do this? 'y' for yes and 'n' for no: \n")
        confirmation = input()
        if confirmation == 'y':
            DeleteData()
        else:
            print("Okay! Data not deleted...")
    elif choice == 6:
        print("Thankyou See You Soon.....Buddy!")
        exit()
    else:
        print("Invalid Choice")
    choice = int(input("Want to perform another operation: if yes then choose from the menu\n"))