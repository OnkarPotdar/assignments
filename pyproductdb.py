## SQLITE DB
import sqlite3

conn=sqlite3.connect(r"/home/dai/Desktop/dai2022/modulewise/AdvProwithPython/assignmentpdffile/assign13database/productdb.db")

if conn!=None:
    print("connection Done...")
else:
    print("Connection not Done...")

choice=0

cursor=conn.cursor()

#display all product
def displayall():
    cursor.execute("select * from product")
    for row in cursor.fetchall():# to retrieve all data
        #print(row)
        print(row[0],"----->",row[1],"----->",row[2],"----->",row[3])

#add new product
def addnewproduct():
    pid=int(input("Enter Product ID: "))
    pname=input("Enter Product Name: ")
    price=float(input("Enter Product Price: "))
    qty=int(input("Enter Product Qty: "))
    
    cursor.execute("insert into product values (?,?,?,?)",(pid,pname,price,qty))
    conn.commit()   

#delete product
def deleteproduct(pid):
    cursor.execute("delete from product where id=?",(pid,))
    conn.commit()

#update product details
def updateproduct(pid):
    pname=input("Enter Product name: ")
    price=float(input("Enter product price: "))
    qty=int(input("Enter product Qty: "))
    cursor.execute("update product name=?,price=?,quantity where id=?",(pname,price,qty,pid))
    conn.commit()
    
#display product details by id
def getbyid(pid):
    cursor.execute("select * from product where id=?",(pid,))
    row=cursor.fetchone() # to retrieve only one data
    return row

#Display all products with quantity > given quantity
def displaybyquantity(qty):
    cursor.execute("select * from product where quantity>?",(qty,))
    for row in cursor.fetchall():# to retrieve all data
        #print(row)
        print(row[0],"----->",row[1],"----->",row[2],"----->",row[3])
    
while choice!=7:
    choice=int(input("""
1. Add new Product
2. Delete Product
3. Update Product
4. Display by ID
5. Display all Products
6. Display all Products with Quantity > given Quantity
7. Exit.
choice: """))

    match choice:
        case 1:#add new product
            addnewproduct()
        
        case 2:#delete product
            pid=int(input("Enter Product ID: "))
            deleteproduct(pid)
        
        case 3:#update product details
            pid=int(input("Enter Product ID: "))
            updateproduct(pid)
        
        case 4:#display details by id
            pid=int(input("Enter Product ID: "))
            row=getbyid(pid)
            print(row[0],"----->",row[1],"----->",row[2],"----->",row[3])
        
        case 5:# display all products
            displayall()
        
        case 6:# Display all products with quantity > given quantity
            qty=int(input("Enter Quantity: "))
            displaybyquantity(qty)
        
        case 7:
            cursor.close() # to close the connection
            conn.close() # to close the connection
            print("Thank You...")
        
        case _:
            print("WRONG CHOICE...")
            
'''data = cursor.execute("select * from product")
for column in data.description:
    print(column)'''
    
