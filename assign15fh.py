###File Handling
from assign15class import *

import os

emplist=[]

#function to read file
def readfile():
    
    if os.path.exists("/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign15filehandling/salariedemployee.dat"):
        with open ("/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign15filehandling/salariedemployee.dat","r") as sfh:
            for ln in sfh:  
                
                ln=ln.rstrip("\n")
                lst=ln.split(",")
                s1=Salariedemp(lst[0],lst[1],lst[2],lst[3],lst[4])
                emplist.append(s1)
                
    if os.path.exists("/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign15filehandling/contractemployee.dat"):
        
        with open ("/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign15filehandling/contractemployee.dat","r") as cfh:  
            for ln in cfh: 
                
                ln=ln.rstrip("\n")
                lst=ln.split(",")
                c1=Contract(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5])
                emplist.append(c1)
    
    else:
        print("file not found...")

#function to write file
def writefile():
    
    if os.path.exists("/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign15filehandling/salariedemployee.dat"):
        with open ("/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign15filehandling/salariedemployee.dat","w") as sfh:
            
            for i in emplist:
                
                if isinstance(i,Salariedemp):
                    j=i.objecttostring()
                    sfh.write(j)
            
    if os.path.exists("/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign15filehandling/contractemployee.dat"):
        with open ("/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign15filehandling/contractemployee.dat","w") as cfh:
            
            for i in emplist:
                
                if isinstance(i,Contract):
                    j=i.objecttostring()
                    cfh.write(j)
     
    else:
        print("file not found...")

#display all employee list
def displayAll():
    for e in emplist:
        print(e)

#function to add new employee
def addnewemployee():
    eid=int(input("Enter ID: "))
    name=input("Enter Name: ")
    dept=input("Enter Department: ")
    desg=input("Enter Designation: ")
    ans=int(input("1. Salaried Employee 2. Contract Employee "))
    if ans==1:
        sal=int(input("Enter Basic Salary: "))
        s1=Salariedemp(eid,name,dept,desg,sal)
        emplist.append(s1)
    else:
        hr=int(input("Enter Work Hours: "))
        charge=int(input("Enter hourly Charges:"))
        c1= Contract(eid,name,dept,desg,hr,charge)
        emplist.append(c1)

#search employee details on empid
def searchEmployee(empid):
    for e in emplist:
        if e.get_id()==empid:
            return e
    else:
        return None

#delete employree from empid
def deleteEmployee(empid):
    e=searchEmployee(empid)
    if e!=None:
        print(e)
        ans=input("do you want to delete (y/n)? ")
        if ans=="y" or ans=="Y":
            emplist.remove(e)readfile()    
    
            return 1
        else:
            return 2
    else:
        return 3

#modify the salary of employee
def modifySalary(empid):eadfile()    
    
    e=searchEmployee(empid)
    if isinstance(e, SalariedEmp):
        s=int(input("Enter Employee Salary: "))
        e.set_sal(s)
        return True
    elif isinstance(e, ContractEmp):
        hr=int(input("Enter hours: "))
        charge=int(input("Enter Charges: "))
        e.set__hr(hr)
        e.set__charge(charge)
        return True
    else:
        return False


#calculate salary of the function
def calculateSalary(empid):
    e=searchEmployee(empid)
    if e!=None:
        return e.calculateSal()
    else:
        return None

readfile()    

choice = 0

while choice != 7:
    choice = int(input("""
    1) Add new Employee
    2) Delete employee
    3) Modify salary of employee
    4) Search employee
    5) Calculate Salary of Employee
    6) Display All
    7) Exit --- write all objects from list into file
    choice?: """))

    match choice:
        case 1:
            addnewemployee()
        
        case 2:eadfile()    
    
            empid=int(input("Enter employee id: "))
            status=deleteEmployee(empid)
            if status==1:
                print("Employee deleted sucessfully..")
            elif status==2:
                print("Employee found but not deleted..")
            else:
                print("Employee Not found..")
        
        case 3:
            empid=int(input("Enter employee id: "))
            status=modifySalary(empid)
            if status:
                print("Employee salary updated sucessfully..")
            else:
                print("Employee Not found..")
        
        case 4:
            empid=int(input("Enter employee id: "))
            status=searchEmployee(empid)
            if status!=None:
                print(f"Employee salary updated sucessfully..\n{status}")
            else:
                print("Employee Not found..")
        
        case 5:
            empid=int(input("Enter employee id: "))
            s=calculateSalary(empid)
            if s!=None:
                print(f"Employee Id: {empid} Salary: {s}")
            else:
                print("Employee Not found..")
 
        case 6:
            displayAll()
        
        case 7:
            writefile()
            print("Thank you for Visiting...")
        
        case _:
            print("Wrong choice enter...")
