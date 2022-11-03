#Database
import sqlite3

conn=sqlite3.connect("userbasedb.db")

if conn!=None:
    print("connection Done...")
else:
    print("Connection not Done...")

cursor=conn.cursor()

#display all user
def displayall():
    cursor.execute("select * from userbase")
    for row in cursor.fetchall():# to retrieve all data
        #print(row)
        print(row[0],"----->",row[1],"----->",row[2],"----->",row[3])

#add new user
def addnewuser():
    uname=input("Enter User Name: ")
    addr=input("Enter User Address: ")
    mob=int(input("Enter User Mobile No: "))
    email=input("Enter User Email Id: ")
    
    cursor.execute("insert into userbase values (?,?,?,?)",(uname,addr,mob,email))
    conn.commit()   

#delete user
def deleteuser(uname):
    cursor.execute("delete from userbase where username=?",(uname,))
    conn.commit()

#update user details
def updateuser(uname):
    addr=input("Enter User Address: ")
    mob=int(input("Enter User Mobile No: "))
    email=input("Enter User Email Id: ")
    
    cursor.execute("update userbase address=?,mobile=?,email=? where username=?",(addr,mob,email,uname))
    conn.commit()
    
#display user details by name
def getbyname(uname):
    cursor.execute("select * from userbase where username=?",(uname,))
    row=cursor.fetchall() # to retrieve only one data
    return row

#display user details by address
def getbyaddress(addr):
    cursor.execute("select * from userbase where address=?",(addr,))
    row=cursor.fetchall() # to retrieve all data
    return row

choice=0
    
while choice!=6:
    choice=int(input("""
1. Add New User
2. Delete User
3. Update User
4. Display by Name
5. Display by Address
6. Display all Users
7. Exit.
choice: """))

    match choice:
        case 1:#add new user
            addnewuser()
        
        case 2:#delete user
            uname=input("Enter User Name: ")
            deleteuser(uname)
        
        case 3:#update user details
            uname=input("Enter User Name: ")
            updateuser(uname)
        
        case 4:#display details by name
            uname=input("Enter User Name: ")
            row=getbyname(uname)
            if len(row)>0:
                for user in row:
                    print(user[0],"----->",user[1],"----->",user[2],"----->",user[3])
            else:
                print("User Name not found...!!!")
                ans=input("Do you want to add new user (y/n): ")
                if ans=="y" or ans=="Y":
                    addnewuser()
                else:
                    print("No User Name address...!!!")    
        
        case 5:#display details by address
            addr=input("Enter User Address: ")
            row=getbyaddress(addr)
            if len(row)>0:
                for user in row:
                    print(user[0],"----->",user[1],"----->",user[2],"----->",user[3])
            else:
                print("User Name not found...!!!")
                ans=input("Do you want to add new user (y/n): ")
                if ans=="y" or ans=="Y":
                    addnewuser()
                else:
                    print("No User Name address...!!!")    

        case 6:# display all user
            displayall()
                
        case 7:
            cursor.close() # to close the connection
            conn.close() # to close the connection
            print("Thank You...")
        
        case _:
            print("WRONG CHOICE...")
          
'''
data = cursor.execute("select * from product")
for column in data.description:
    print(column)
    
'''