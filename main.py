def AddData():
    print("Enter the Following details about the employee please: ")
    sfid = input("Enter the SFID of Employee: \n")
    name = input("Enter the name of Employee: \n")
    email = input("Enter email id: \n")
    designation = input("Position in the company: \n")
    phno = input("Enter Phone number: \n")
    file.write(sfid+"   "+name+"    "+email+"   "+designation+"    "+phno+"\n")
    print("Data added successfully!....")


file = open("EmployeeData.txt", "at")
print('''
********** Welcome to L&T Employee Management Service **********

******************************MENU******************************

                          1. ADD DATA    

                          2. VIEW DATA     

                          3. EXIT                          ''')

choice = int(input("What you want to do with database, make a choice: "))

while choice != 0:
    if choice == 1:
        while(choice == 1):
            AddData()
            choice = int(input("Want to add Another Entry: 1 for yes and 0 for no\n"))
    elif choice == 2:
        print("Display Function called")
        file = open("EmployeeData.txt", 'r')
        content = file.read()
        print(content)
    elif choice == 3:
        print("Exit Function Called")
        exit()
    else:
        print("Invalid Choice")
    choice = int(input("Want to perform another operation: if yes then choose from the menu\n"))
file.close()