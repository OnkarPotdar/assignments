from studentclass import *

studentlist=[]
namelist=[]

# function to add student in list
def addStudent():
    name=input("Enter Student Name: ")
    m1=int(input("Enter Marsk of M1: "))
    m2=int(input("Enter Marsk of M2: "))
    m3=int(input("Enter Marsk of M3: "))
    S=Student(name,m1,m2,m3)
    studentlist.append(S)

#display all student list
def displayAll():
    for s in studentlist:
        print(s)

#search Student by ID
def searchById(sid):
    for student in studentlist:
        if student.get_sid()==sid:
            return student
    else:
        return None

#search Student by Name
def searchByName(sname):
    for student in studentlist:
        if student.get_name()==sname:
            namelist.append(student)
    return namelist

#calculate GPA of student on SID search
def calculateGPA(sid):
    stud=searchById(sid)
    if stud!=None:
        return stud.gpaCalculation()
    else:
        return None

choice=0

while choice!=6:
    choice=int(input("""
                        1. Add Student
                        2. Display All Student
                        3. Search by id
                        4. Search by name
                        5. calculate GPA of a student
                        6. Exit
                        choice: """))
    
    match(choice):
        case 1:
            addStudent()
            
        case 2:
            displayAll()
        
        case 3:
            sid=input("Enter Student ID: ")
            stud=searchById(sid)
            if stud!=None:
                print(f"Student Search Complete... \n {stud}")
            else:
                print("Student not found...")
        
        case 4:
            sname=input("Enter Student Name: ")
            stud=searchByName(sname)
            if len(stud)>0:
                print(f"Student Search Complete...")
                for name in stud:
                    print(name)
            else:
                print("Student not found...")
        
        case 5:
            sid=input("Enter Student ID to calculate GPA: ")
            gpa=calculateGPA(sid)
            if gpa!=None:
                print(f"Student ID: {sid} \nGPA: {gpa}")
            else:
                print("Student not found...")
          
        case 6:
            print("Thank you for visit...")
        
        case _:
            print("Wrong Choice...")
