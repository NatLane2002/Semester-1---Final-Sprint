import csv

# Constants from defaults file
EMPLOYEE_FILE = 'employees.csv'
CUSTOMER_FILE = 'customers.csv'
INVENTORY_FILE = 'inventory.csv'
SALES_FILE = 'sales.csv'
REORDER_FILE = 'reorder.csv'

# Function to read from file and return list of dictionaries
def read_file(file):
    with open(file, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

# Function to write list of dictionaries to file
def write_file(file, data):
    with open(file, mode='w', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Function to record customer purchase
def record_purchase():
    inventory = read_file(INVENTORY_FILE)
    customers = read_file(CUSTOMER_FILE)
    sales = read_file(SALES_FILE)

    print("Enter Purchase Details:")
    customer_id = input("Customer ID: ")
    item_id = input("Item ID: ")
    quantity = int(input("Quantity: "))

    # Check if customer and item exist
    customer = next((c for c in customers if c['ID'] == customer_id), None)
    item = next((i for i in inventory if i['ID'] == item_id), None)

    if not customer:
        print("Customer not found.")
        return
    if not item:
        print("Item not found.")
        return
    if quantity > int(item['Quantity']):
        print("Not enough stock available.")
        return

    # Calculate subtotal and commission
    price = float(item['Price'])
    subtotal = price * quantity
    commission_rate = 0.06
    commission = subtotal * commission_rate
    if subtotal > 5000:
        commission += 200

    # Update inventory and sales
    item['Quantity'] = str(int(item['Quantity']) - quantity)
    sale = {'Customer ID': customer_id, 'Item ID': item_id, 'Quantity': str(quantity), 'Subtotal': str(subtotal)}
    sales.append(sale)

    # Save changes to files
    write_file(INVENTORY_FILE, inventory)
    write_file(SALES_FILE, sales)

    # Display purchase details
    print("\nPurchase Details:")
    print("Customer Name:", customer['Name'])
    print("Item Name:", item['Name'])
    print("Quantity:", quantity)
    print("Price per item:", price)
    print("Subtotal:", subtotal)
    print("Commission:", commission)

# Main program
while True:
    print("\nSimpson Carpet World Company Services System")
    print("1. Enter a New Employee.")
    print("2. Enter a New Customer.")
    print("3. Enter a New Inventory Item.")
    print("4. Record Customer Purchase.")
    print("5. Print Employee Listing.")
    print("6. Print Customers by Branch.")
    print("7. Print Orders By Customer.")
    print("8. Print Reorder Listing.")
    print("9. Quit Program.")

    choice = input("Enter choice (1-9): ")
    if choice == '1':
        # Code for entering new employee
        pass
    elif choice == '2':
        # Code for entering new customer
        pass
    elif choice == '3':
        # Code for entering new inventory item
        pass
    elif choice == '4':
        record_purchase()
    elif choice == '5':
