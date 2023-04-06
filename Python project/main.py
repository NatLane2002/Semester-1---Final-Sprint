# Database management system for Simpson’s Carpet World to keep a track of sales, customers, and employees
# Created by: Robot group 4
# Date created: Apr-03-2023


# open the defaults file and assign variables
defaults = open("defaults.dat", "r")
employeeID = int(defaults.readline())
custNumber = int(defaults.readline())
invID = int(defaults.readline())
PROVINCES = defaults.readline().split(",")
defaults.close()


def NewEmp():
    pass


def NewCust():
    global custNumber, PROVINCES
    while True:
        custFirstName = input("Enter customer's first name: ").title()
        if custFirstName != "":
            break
        else:
            print("Please enter a name")

    while True:
        custLastName = input("Enter customer's last name: ").title()
        if custLastName != "":
            break
        else:
            print("Please enter a name")
    custAddress = input("Enter customer's street address: ").title()
    custCity = input("Enter customer's city: ").capitalize()

    while True:
        custProvince = input("Enter customer's province: ").upper()
        if custProvince in PROVINCES:
            break
        else:
            print('Province must be from list: ')

    custPostalCode = input("Enter customer's postal code: ").upper()
    custHomePhone = input("Enter customer's home phone number: ")
    custCellPhone = input("Enter customer's cell phone number: ")
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

    # update customer number and write values back to defaults file
    custNumber += 1
    f = open('defaults.dat', 'w')
    f.write(f'{employeeID}\n')
    f.write(f'{custNumber}\n')
    f.write(f'{invID}')
    f.write(f'{PROVINCES}')


# Create a function for option 3 of the menu
def NewInIt():

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
                print(f"Item maximum level cannot be less than 1 or {ItemReorderPoint} - please reenter")
                continue
        except:
            print()
            print("Must enter a valid number")
        else:
            break

    f = open("NewInvItem.dat", "a")

    f.write("{}, ".format(str(ItemDescription)))
    f.write("{}, ".format(str(ItemColour)))
    f.write("{}, ".format(str(ItemSize)))
    f.write("{}, ".format(str(ItemPattern)))
    f.write("{}, ".format(str(ItemType)))
    f.write("{}, ".format(str(ItemCost)))
    f.write("{}, ".format(str(ItemRetailPrice)))
    f.write("{}, ".format(str(ItemQOH)))
    f.write("{}, ".format(str(ItemReorderPoint)))
    f.write("{}\n".format(str(ItemMaxLvl)))
    f.close()

def RecCustPur():
    pass


def PrintEmpList():
    pass


def PrintCustByBran():
    pass


def PrintOrdByCust():
    pass


def PrintReordList():
    pass


def QuitProg():
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
    print()
    print("9. Quit Program")
    print()
    Choice = int(input("  Enter Choice (1-9): ").title())

    # Start of main program
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
