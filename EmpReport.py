#Option 5
#Author: Dawson Murray
#Date: April 6 2023

#Import
import datetime
import FormatValues as FV


#Get Current day
CurDate = datetime.date.today()

#Format Current day as YYYY-MM-DD
FormattedDate = CurDate.strftime('%Y-%b-%d')

#Employee counter
EmployeeCounter = 0


#Inputs for Testing
EMP_NUM = 12
'''
EmpName = ("John Smith")
Add = ("22 Church Road")
City = ("Badger")
ProvState = ("NL")
PostCode = ("A0H1A0")
PhoneNum = 7091234567
HireDate = "2022-Jan-21"
Branch = "Sales"
Title = "Salesman"
Salary = 90000
Skill = "Beautiful and smart"
BirthDay = "2002-May-13"
'''

#Print Report Heading and information
print()
print("Simpson's Carpet World")
print("482 Torbay Road")
print("(709)123-4567")
print()
print(f"Employee Listing Report for {(FormattedDate)}")
print("---------------------------------------")

print()

print("Emp   Emp          Phone        Hire          Emp       Emp        Emp        Birth")
print("Num   Name         Number       Date          Branch    Title      Salary     Date")
print("=========================================================================================")


f = open("NewEmp.dat", "r")

for NewEmpLine in f:
        NewEmpLine = NewEmpLine.strip("\n")
        SplitNewEmpLine = NewEmpLine.split(",")

        #EMP_NUM = (NewImpLine[0].strip())
        EmpName = (SplitNewEmpLine[0].strip())
        Add = (SplitNewEmpLine[1].strip())
        City = (SplitNewEmpLine[2].strip())
        ProvState = (SplitNewEmpLine[3].strip())
        PostCode = (SplitNewEmpLine[4].strip())
        PhoneNum = (SplitNewEmpLine[5].strip())
        HireDate = (SplitNewEmpLine[6].strip())
        Branch = (SplitNewEmpLine[7].strip())
        Title = (SplitNewEmpLine[8].strip())
        Skill = (SplitNewEmpLine[9].strip())
        BirthDay = (SplitNewEmpLine[10].strip())
        Salary = (SplitNewEmpLine[11].strip())

        #Employee Counter
        EmployeeCounter += 1

        
        print(f"{EMP_NUM:<4}  {EmpName:<12} {PhoneNum:<13}{HireDate:<10}   {Branch:<8}  {Title:<8}   ${Salary:<10}{BirthDay:<10}")

        print()
        print(f"Employee Address: {Add}, {City}, {ProvState}, {PostCode}")
        print(f"Employee Skills: {Skill}")
        

print()

print("=========================================================================================")
print(f"Total Employees: {EmployeeCounter:<4} ")

print()


'''
def NewEmp():
    f = open("NewImpDef.dat", "r")
    EMP_NUM = int(f.readline())
    f.close()
    EmpName = input("Enter the employees first and last name: ")
    Add = input("Enter the employees street address: ")
    City = input("Enter the City: ")
    ProvState = input("Enter the province or state: ")
    PostCode = input("Enter the employees postal code: ")
    PhoneNum = input("Enter the employees phone number: ")
    HireDate = input("Enter the date of hire: ")
    Branch = input("Enter the branch: ")
    Title = input("Enter the title: ")
    Salary = input("Enter Employee Salary: ")
    Skill = input("Enter the employees skill(s): ")
    BirthDay = input("Enter the employees birth date: ")
    print(EmpName)
    print(Add)
    print(City)
    print(ProvState)
    print(PostCode)
    print(PhoneNum)
    print(HireDate)
    print(Branch)
    print(Title)
    print(Skill)
    print(BirthDay)
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
    '''