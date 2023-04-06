"""
Description: Option two of the menu for the final sprint

Author: Nathaniel Lane
Date: April 5th, 2023
"""

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

NewInIt()
