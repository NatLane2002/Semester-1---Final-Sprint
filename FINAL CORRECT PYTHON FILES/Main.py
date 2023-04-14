# Database management system for Simpson’s Carpet World to keep a track of sales, customers, and employees
# Created by: Robot group 4
# Date created: Apr-03-2023

# Import datetime library
import datetime

# Import FormatValues library as FV
import FormatValues as FV

# Import time library
import time

# open the defaults file and assign variables
defaults = open("defaults.dat", "r")

employeeID = int(defaults.readline())
custNumber = int(defaults.readline())
# This is the comma separated provinces which need to be written back to the defaults file at the end of each program
Provinces = defaults.readline()
ItemNum = int(defaults.readline())

# This is the list of provinces
PROVINCES = Provinces.split(",")

defaults.close()

def NewEmp():  

    global employeeID                                                                                                                                           

    print()
    EmpName = input("Enter the employees first and last name: ").capitalize()
    print()
    Add = input("Enter the employees street address: ")
    print()
    City = input("Enter the City: ").title()
    print()
    ProvState = input("Enter the province or state: ").upper()
    print()
    PostCode = input("Enter the employees postal code: ").upper()
    print()
    PhoneNum = input("Enter the employees phone number: ")
    print()
    HireDate = input("Enter the date of hire: ")
    print()
    Branch = input("Enter the branch: ")
    print()
    Title = input("Enter the title: ")
    print()
    Salary = float(input("Enter the employees salary: "))
    print()
    Skill = input("Enter the employees skill(s): ")
    print()
    BirthDay = input("Enter the employees birth date: ")
    print()
    Dependants = input("Enter the employees dependants: ")

    f = open("NewEmp.dat", "a")

    f.write("{}, ".format(str(employeeID)))
    f.write("{}, ".format(str(EmpName)))
    f.write("{}, ".format(str(Add)))
    f.write("{}, ".format(str(City)))
    f.write("{}, ".format(str(ProvState)))
    f.write("{}, ".format(str(PostCode)))
    f.write("{}, ".format(str(PhoneNum)))
    f.write("{}, ".format(str(HireDate)))
    f.write("{}, ".format(str(Branch)))
    f.write("{}, ".format(str(Title)))
    f.write("{}, ".format(str(Salary)))
    f.write("{}, ".format(str(Skill)))
    f.write("{}, ".format(str(BirthDay)))
    f.write("{}\n".format(str(Dependants)))
    f.close()

    print()
    print("Saving information...")

    time.sleep(2)

    print()
    print("New employee information processed and saved ")

    employeeID += 1
    # update customer number and write values back to defaults file
    f = open('defaults.dat', 'w')
    f.write(f'{employeeID}\n')
    f.write(f'{custNumber}\n')
    f.write(f'{Provinces}')
    f.write(f'{ItemNum}')

def NewCust():

    global custNumber, PROVINCES

    while True:
        print()
        custFirstName = input("Enter customer's first name: ").title()
        if custFirstName != "":
            break
        else:
            print("Please enter a name")

    while True:
        print()
        custLastName = input("Enter customer's last name: ").title()
        if custLastName != "":
            break
        else:
            print("Please enter a name")

    print()
    custAddress = input("Enter customer's street address: ").title()

    print()
    custCity = input("Enter customer's city: ").capitalize()

    while True:
        print()
        custProvince = input("Enter customer's province: ").upper()
        if custProvince in PROVINCES:
            break
        else:
            print('Province must be from list: ')

    print()
    custPostalCode = input("Enter customer's postal code: ").upper()

    print()
    custHomePhone = input("Enter customer's home phone number: ")

    print()
    custCellPhone = input("Enter customer's cell phone number: ")

    print()
    custDateOfBirth = input("Enter customer's date of birth (DD-MM-YYYY): ")

    # write values to customers.dat
    f = open('customer.dat', 'a')
    f.write(f'{custNumber}, ')
    f.write(f'{custFirstName}, ')
    f.write(f'{custLastName}, ')
    f.write(f'{custAddress}, ')
    f.write(f'{custCity}, ')
    f.write(f'{custProvince}, ')
    f.write(f'{custPostalCode}, ')
    f.write(f'{custHomePhone}, ')
    f.write(f'{custCellPhone}, ')
    f.write(f'{custDateOfBirth}\n')
    f.close()

    print()
    print("Saving information...")

    time.sleep(2)

    print()
    print("New customer information processed and saved")

    # update customer number and write values back to defaults file
    custNumber += 1
    f = open('defaults.dat', 'w')
    f.write(f'{employeeID}\n')
    f.write(f'{custNumber}\n')
    f.write(f'{Provinces}')
    f.write(f'{ItemNum}')

# Create a function for option 3 of the menu
def NewInIt():

    # Declare ItemNum as a global scoped variable
    global ItemNum

    # Get the user to input all of the necessary information to be added to the NewInvItem.dat file

    # Get the item description from the user
    print()
    ItemDescription = input("Item description: ")

    # Get the item colour from the user
    print()
    ItemColour = input("Item colour: ")

    # Get the item size from the user
    print()
    ItemSize = input("Item size: ")

    # Get the item pattern from the user
    print()
    ItemPattern = input("Item pattern: ")

    # Get the item type from the user
    print()
    ItemType = input("Item type: ")

    # Get the item cost from the user
    while True:
        print()
        ItemCost = input("Item cost: ")
        try:
            ItemCost = float(ItemCost)
            if ItemCost < 0:
                print()
                print("Must enter a positive number - please reenter")
                continue
        except:
            print()
            print("Must enter a valid number")
        else:
            break

    # Get the item retail price from the user
    while True:
        print()
        ItemRetailPrice = input("Item retail price: ")
        try:
            ItemRetailPrice = float(ItemRetailPrice)
            if ItemRetailPrice < 0:
                print()
                print("Must enter a positive number - please reenter")
                continue
        except:
            print()
            print("Must enter a valid number")
        else:
            break

    # Get the item's quantity on hand from the user
    while True:
        print()
        ItemQOH = input("Item QOH: ")
        try:
            ItemQOH = int(ItemQOH)
            if ItemQOH < 0:
                print()
                print("Must enter a positive number - please reenter")
                continue
        except:
            print()
            print("Must enter a valid number")
        else:
            break

    # Get the item's reorder point from the user
    while True:
        print()
        ItemReorderPoint = input("Item reorder point: ")
        try:
            ItemReorderPoint = int(ItemReorderPoint)
            if ItemReorderPoint < 0:
                print()
                print("Must enter a positive number - please reenter")
                continue
        except:
            print()
            print("Must enter a valid number")
        else:
            break

    # Get the item's maximum level from the user
    while True:
        print()
        ItemMaxLvl = input("Item maximum level: ")
        try:
            ItemMaxLvl = int(ItemMaxLvl)
            if ItemMaxLvl < 1 or ItemMaxLvl < ItemReorderPoint:
                print()
                print(f"Item maximum level cannot be less than {ItemReorderPoint} - please reenter")
                continue
            if ItemMaxLvl < ItemQOH:
                print()
                print("Item's maximum level must be greater than or equal to the quantity on hand - please reenter")
                continue
        except:
            print()
            print("Must enter a valid number")
        else:
            break

    print()
    OrderInformation = input("Order information: ")

    # Print calculated values for the user
    print()
    if ItemQOH < ItemReorderPoint:
        print(f"{ItemMaxLvl - ItemQOH} of these items need to be ordered.")
    else:
        print("This item does not need to be reordered.")

    print()
    print(f"The retail cost after taxes is {FV.FDollar2(ItemRetailPrice * 1.15)}.")

    f = open("NewInvItem.dat", "a")

    f.write("{}, ".format(str(ItemNum)))
    f.write("{}, ".format(str(ItemDescription)))
    f.write("{}, ".format(str(ItemColour)))
    f.write("{}, ".format(str(ItemSize)))
    f.write("{}, ".format(str(ItemPattern)))
    f.write("{}, ".format(str(ItemType)))
    f.write("{}, ".format(str(ItemCost)))
    f.write("{}, ".format(str(ItemRetailPrice)))
    f.write("{}, ".format(str(ItemQOH)))
    f.write("{}, ".format(str(ItemReorderPoint)))
    f.write("{}, ".format(str(ItemMaxLvl)))
    f.write("{}\n".format(str(OrderInformation)))

    f.close()

    print()
    print("Saving information...")

    time.sleep(2)

    print()
    print("New item information processed and saved ")

    # Increment the ItemNum by 1
    ItemNum += 1

    # Update the ItemNum in the defaults file
    f = open("defaults.dat", "w")

    f.write(f'{employeeID}\n')
    f.write(f'{custNumber}\n')
    f.write(f'{Provinces}')
    f.write(f'{ItemNum}')

    f.close()

def RecCustPur():
    print()
    print("----------------------")
    print("Funtion not available.")
    print("----------------------")

def PrintEmpList():
    #Get Current day
    CurDate = datetime.date.today()

    #Format Current day as YYYY-MM-DD
    FormattedDate = CurDate.strftime('%Y-%b-%d')

    print()
    print("Printing employee listing report...")
    print()

    time.sleep(2)

    #Employee counter
    EmployeeCounter = 0

    #Print Report Heading and information
    print()
    print("Simpson's Carpet World")
    print("482 Torbay Road")
    print("(709)123-4567")
    print()
    print(f"Employee Listing Report for {FormattedDate}")
    print("---------------------------------------")

    print()

    print("Emp   Emp               Phone        Hire         Emp              Emp                    Emp        Birth")
    print("Num   Name              Number       Date         Branch           Title                  Salary     Date")
    print("================================================================================================================")

    f = open("NewEmp.dat", "r")

    for NewEmpLine in f:

        NewEmpLine = NewEmpLine.strip("\n")
        SplitNewEmpLine = NewEmpLine.split(",")

        employeeID = (SplitNewEmpLine[0].strip())
        EmpName = (SplitNewEmpLine[1].strip())
        Add = (SplitNewEmpLine[2].strip())
        City = (SplitNewEmpLine[3].strip())
        ProvState = (SplitNewEmpLine[4].strip())
        PostCode = (SplitNewEmpLine[5].strip())
        PhoneNum = (SplitNewEmpLine[6].strip())
        HireDate = (SplitNewEmpLine[7].strip())
        Branch = (SplitNewEmpLine[8].strip())
        Title = (SplitNewEmpLine[9].strip())
        Salary = (SplitNewEmpLine[10].strip())
        Skill = (SplitNewEmpLine[11].strip())
        BirthDay = (SplitNewEmpLine[12].strip())
        Dependants = (SplitNewEmpLine[13].strip())

        EmployeeCounter += 1

        print(f"{employeeID:<4}  {EmpName:<17} {PhoneNum:<13}{HireDate:<10}   {Branch:<15}  {Title:<22} ${Salary:<10}{BirthDay:<10}")
        print(f"Employee Address:                                         {Add:>20}, {City:>19}, {ProvState:>2}, {PostCode:>6}")
        print(f"Employee Skills: {Skill:>94}")
        print()

    print("================================================================================================================")
    print(f"Total Employees: {EmployeeCounter:<4} ")
    print()

def PrintCustByBran():
    print()
    print("----------------------")
    print("Funtion not available.")
    print("----------------------")

def PrintOrdByCust():
    print()
    print("----------------------")
    print("Funtion not available.")
    print("----------------------")

def PrintReordList():
    # Date as of today
    today = datetime.date.today()

    print()
    print("Printing reorder listing report...")
    print()

    time.sleep(2)

    totalItemsOrdered = 0
    totalCost = 0

    # Open and Read Data file
    f = open("NewInvItem.dat", "r")

    # Print headings
    print("Simpson's Carpet World")
    print("482 Torbay Road")
    print("(709)123-4567")
    print()
    print(f"Reorder listing report for {today}")
    print()
    print(f"Item    Item                         Item      Item   Order       Order")
    print(f"Number  Description                  Colour    Size   Quantity    Date")
    print("=" * 77)

    # Go through data file
    for inventoryData in f:

        inventoryData = inventoryData.strip("\n")
        splitInventoryData = inventoryData.split(",")

        itemNumber = splitInventoryData[0].strip()
        itemDescription = splitInventoryData[1].strip()
        itemColor = splitInventoryData[2].strip()
        itemSize = splitInventoryData[3].strip()
        itemPattern = splitInventoryData[4].strip()
        itemType = splitInventoryData[5].strip()
        itemCost = splitInventoryData[6].strip()
        itemRetailCost = splitInventoryData[7].strip()
        itemQOH = splitInventoryData[8].strip()
        itemReorderPoint = splitInventoryData[9].strip()
        itemMaxLevel = splitInventoryData[10].strip()
        orderInformation = splitInventoryData[11].strip()

        if itemQOH <= itemReorderPoint:
            # Print outputs
            print(f"{itemNumber:<5}   {itemDescription:<25}    {itemColor:<8}  {itemSize:<4}   {itemQOH:<4}        {str(today):>10}")
            print(f"Order Information: {orderInformation:<60}")
            print()

            totalItemsOrdered += 1
            itemCost = float(itemCost)
            totalCost += itemCost

    print("=" * 77)
    print(f"Total Items Ordered: {totalItemsOrdered:<5}                            Total Cost: {FV.FDollar2(totalCost):>10}")
    print()

def QuitProg():
    print()
    exit()

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
    print("8. Print Reorder Listing")
    print()
    print("9. Quit Program")
    print()
    Choice = input("  Enter Choice (1-9): ")

    # Start of main program
    if Choice == '1':
        NewEmp()
    elif Choice == '2':
        NewCust()
    elif Choice == '3':
        NewInIt()
    elif Choice == '4':
        RecCustPur()
    elif Choice == '5':
        PrintEmpList()
    elif Choice == '6':
        PrintCustByBran()
    elif Choice == '7':
        PrintOrdByCust()
    elif Choice == '8':
        PrintReordList()
    elif Choice == '9':
        QuitProg()
    else:
        print()
        print("Must enter a valid option - please reenter")