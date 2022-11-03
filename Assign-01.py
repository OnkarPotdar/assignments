# assignment 1 - if Statements

#Q-1.

classes=int(input("Enter numbers of classes held: "))
attendance=int(input("Enter numbers of the classes attended: "))

percent_attendence=(attendance*100)/classes

if percent_attendence>=75:
    print(f"student attendence is {percent_attendence}% and is allowed to the give Exams..")
else:
    print(f"student attendence is {percent_attendence}% and is NOT allowed to the give Exams..")


#Q-2.

amount=int(input("Enter the amount to denominate: "))
a=amount//2000
amount=amount%2000
b=amount//500
amount=amount%500
i=amount//200
amount=amount%200
c=amount//100
amount=amount%100
d=amount//50
amount=amount%50
j=amount//20
amount=amount%20
e=amount//10
amount=amount%10
f=amount//5
amount=amount%5
g=amount//2
amount=amount%2
h=amount//1
amount=amount%1

if a>0:
    print("Note 2000 =",a)
if b>0:
    print("Note 500 =",b)
if i>0:
    print("Note 200 =",i)
if c>0:
    print("Note 100 =",c)
if d>0:
    print("Note 50 =",d)
if j>0:
    print("Note 20 =",j)
if e>0:
    print("Note 10 =",e)
if f>0:
    print("Note 5 =",f)
if g>0:
    print("Note 2 =",g)
if h>0:
    print("Note 1 =",h)
else:
    pass

#Q-3.

classes=int(input("Enter numbers of lectures scheduled: "))
attendance=int(input("Enter number of lectures attended: "))

percent_attended=(attendance*100)/classes

if percent_attended>=75:
    print(f"student attendence is {percent_attended}% and is allowed to give Exams..")
else:
    medical=input("Is student having valid medical cause (y/n)?")
    if medical=="y":
        print(f"student attendence is {percent_attended}%")
        print("Due to medical cause student is allowed to give Exams..")
    else:
        print(f"student attendence is {percent_attended}% and is NOT allowed to give Exams..")

#Q-4.

mark=int(input("Enter your marks: "))

if mark>80:
    print(f"Marks = {mark} and Grade = A, Congratulations!")
elif mark>60:
    print(f"Marks = {mark} and Grade = B")
elif mark>50:
    print(f"Marks = {mark} and Grade = C")
elif mark>45:
    print(f"Marks = {mark} and Grade = D")
elif mark>25:
    print(f"Marks = {mark} and Grade = E, Failed.")
else:
    print(f"Marks = {mark} and Grade = F, Failed.")

#Q-5.
x=2
y=5
z=0

print("a. x==2: ",x==2)
print("b. x!=5: ",x!=5)
print("c. x!=5 && y>=5: ",x!=5 and y>=5)
print("d. z!=0 || x==2: ",z!=0 or x==2)
if not(y<10):
    print("True")
else:
    print("False")


#Q-6.

num=int(input("Enter the number: "))

if num%5==0 and num%11==0:
    print(f"Number {num} is divisible by 5 and 11.")
else:
    print(f"Number {num} is NOT divisible by 5 and 11.")


#Q-7.
unit=int(input("Enter the Units of Electricity consumed: "))
bill=0

if unit>200:
    bill=(unit-200)*10+(100*5)
    print(f"Electricity bill for {unit} units is: Rs.{bill}")
elif unit>100:
    bill=(unit-100)*5
    print(f"Electricity bill for {unit} units is: Rs.{bill}")
else:
    print(f"Electricity bill for {unit} units is: Rs.{bill}")

#Q-8.
num = int(input("Enter a number:"))
n= num % 10
if n % 3 == 0:
    print(f"Last digit {n} is divisible by 3")
else:
    print(f"Last digit {n} is not divisible by 3")

#Q-9.

year = int(input("Enter year to check leap year :"))

if year%400==0 :
    print(f"{year} is a leap year")
elif year%4==0 and year%100!=0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")


#Q-10.

price = int(input("Enter the price of a bike :"))
if price > 100000:
    tax = price * 0.15
    insurance = price * 0.20
    print(f"Tax of bike is {tax} and insurance of bike is {insurance} and total price of bike is {tax + insurance + price}")
elif price <= 100000 and price > 50000:
    tax = price * 0.10
    insurance = price * 0.08
    print(f"Tax of bike is {tax} and insurance of bike is {insurance} and total price of bike is {tax + insurance + price}")
else:
    tax = price * 0.05
    insurance = price * 0.05
    print(f"Tax of bike is {tax} and insurance of bike is {insurance} and total price of bike is {tax + insurance + price}")



















