import csv

# Define constants
SALES_FILE = 'sales.csv'
EMPLOYEES_FILE = 'employees.csv'
COMMISSION_RATE = 0.06
BONUS_THRESHOLD = 5000
BONUS_AMOUNT = 200

# Define variables
employee_sales = {}

# Read sales data from file
with open(SALES_FILE, 'r') as sales_file:
    sales_reader = csv.DictReader(sales_file)
    for row in sales_reader:
        employee = row['Employee']
        subtotal = float(row['Subtotal'])
        if employee not in employee_sales:
            employee_sales[employee] = subtotal
        else:
            employee_sales[employee] += subtotal

# Calculate commissions and bonuses
employee_commissions = {}
for employee, sales in employee_sales.items():
    commission = sales * COMMISSION_RATE
    if sales >= BONUS_THRESHOLD:
        commission += BONUS_AMOUNT
    employee_commissions[employee] = commission

# Read employee data from file
with open(EMPLOYEES_FILE, 'r') as employees_file:
    employees_reader = csv.DictReader(employees_file)
    employees = {row['ID']: row['Name'] for row in employees_reader}

# Output results
print('Commission Report:')
print('------------------')
for employee_id, name in employees.items():
    if name in employee_commissions:
        commission = employee_commissions[name]
        print(f'{name}: ${commission:.2f}')
    else:
        print(f'{name}: No sales this month')
