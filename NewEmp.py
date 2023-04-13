def NewEmp():

    EMP_NUM = 56

    EmpName = input("Enter the employees first and last name: ")
    Add = input("Enter the employees street address: ")
    City = input("Enter the City: ")
    ProvState = input("Enter the province or state: ")
    PostCode = input("Enter the employees postal code: ")
    PhoneNum = input("Enter the employees phone number: ")
    HireDate = input("Enter the date of hire: ")
    Branch = input("Enter the branch: ")
    Title = input("Enter the title: ")
    Salary = float(input("Enter the employees salary: "))
    Skill = input("Enter the employees skill(s): ")
    BirthDay = input("Enter the employees birth date: ")
    Dependants = input("Enter the employees dependants: ")

    print(EmpName)
    print(Add)
    print(City)
    print(ProvState)
    print(PostCode)
    print(PhoneNum)
    print(HireDate)
    print(Branch)
    print(Title)
    print(Salary)
    print(Skill)
    print(BirthDay)
    print(Dependants)

    f = open("NewEmp.dat", "a")

    f.write("{}, ".format(str(EMP_NUM)))
    f.write("{}, ".format(EmpName))
    f.write("{}, ".format(Add))
    f.write("{}, ".format(City))
    f.write("{}, ".format(ProvState))
    f.write("{}, ".format(PostCode))
    f.write("{}, ".format(PhoneNum))
    f.write("{}, ".format(HireDate))
    f.write("{}, ".format(Branch))
    f.write("{}, ".format(Title))
    f.write("{}, ".format(Skill))
    f.write("{}\n".format(BirthDay))
    f.close()

    print()
    print("New employee information processed and saved ")

    EMP_NUM += 1

def NewCust():
    pass

def NewInIt():
    pass

def  RecCustPur():
    pass

def  PrintEmpList():
    pass

def  PrintCustByBran():
    pass

def  PrintOrdByCust():
    pass

def  PrintReordList():
    pass

def QuitProg():
    pass

# Title and menu
while True:

    print()
    print("Simpson Carpet World")
    print("Company Services System")
    print()
    print("1. Enter a New Employee.")
    print("2. Enter a New Customer.")
    print("3. Enter a New Inventory Item.")
    print()
    print("4. Record Customer Purchase.")
    print()
    print("5. Print Employee Listing.")
    print("6. Print Customers By Branch.")
    print("7. Print Orders By Customer")
    print()
    print("9. Quit Program")
    print()

    # Start of main program
    Choice = int(input("Enter choice(1-9): "))
    if Choice == 1:
        NewEmp()
    elif Choice == 2:
        NewCust()
    elif Choice == 3:
        NewInIt()
    elif Choice == 4:
        RecCustPur()
    elif Choice == 5:
        PrintEmpList()
    elif Choice == 6:
        PrintCustByBran()
    elif Choice == 7:
        PrintOrdByCust()
    elif Choice == 8:
        PrintReordList()
    elif Choice == 9:
        QuitProg()
    else:
        break
