# Assignment 02 - For and While loop

#Q-1. average of 10 numbers
avg=0
sum=0

for i in range(10):
    num=int(input(f"Enter number {i+1} = "))
    sum=sum+num
avg=sum/10
print("Average of 10 numbers are = ",avg)

            
#Q-2.(a) triangle of stars (*)

for j in range(6):
    print("*"*j)



#Q-2.(b) Odd diamond of stars (*)

row=int(input("Enter rows: "))
for i in range(1,row+1):
    if i%2!=0:
        print(" "*((row-i)//2),"*"*i)
for i in range(row-2,0,-1):
    if i%2!=0:
        print(" "*((row-i)//2),"*"*i)



#Q-2.(c) Shape invert diamond of 101010101

row=int(input("Enter the row: "))
for i in range(1,row+1):
    if i%2!=0:
        for j in range(1,row-i+2):
            if j%2!=0:
                print("1",end="")
            else:
                print("0",end="")
        print()



#Q-2.(d) Triangle of number

row=int(input("Enter the row: "))

for j in range(1,row+1):
    for i in range(1,j+1):
        print(i,end="")
    print()



#Q-3. find highest common factor HCF

a=int(input("Enter number a : "))
b=int(input("Enter number b : "))

for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        break
print(f"HCF of numbers {a} and {b} is = ",i)



#Q-4. Print sum, product and use "q" to exit program condition 01

ans="a"
sum=0
avg=0
product=1
count=0

while ans!="q" or ans!="Q":
    x=int(input("Enter the number:"))
    sum=sum+x
    count=count+1
    average=sum/count
    product=product*x
    print(f"average= {average} and product= {product}")
    ans=input()
    if ans=="q" or ans=="Q":
        break
print("Exit of while loop")



#Q-5. Enter number, count digits of number and sum of the digits:

sum=0
rem=0
count=0
number=int(input("Enter the number: "))
numbercopy=number
while number>0:
    rem=number%10
    sum=sum+rem
    number=number//10
    count=count+1
if numbercopy!=0:
    print(f"Number {numbercopy} have {count} of digits and sum is {sum}")
else:
    print(f"Number {numbercopy} has 1 digit and sum is {sum}")





#Q-6. print cube of given integers

number=int(input("Enter the number: "))

for i in range(1,number):
    print(i**3, end=" ")



#Q-7. Sum of even numbers from 20 inputs

s=0
for i in range(1,21):
    num = int(input(f"Enter num {i}: "))
    if num % 2 == 0:
        s=s+num
print("Summation of given even numbers is ",s)



#Q-8.  print the series

n=int(input("Enter number of terms: "))
digit=int(input("Enter digit: "))
sum=0
num=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{digit}",end="")
    print(end="+")

for i in range(1,n+1):
    num=int(f"{digit}"*i)
    sum=sum+num

print(f"\nsum = {sum}")



#Q-9. print series solution 1+x+x^2/2!+.... condition 01

import math

sum =0
x = int(input("Input the value of x : "))
n = int(input("Input the number of terms : "))
for i in range(0,n):
   sum = sum + ((x**i)/math.factorial(i))
print(f"sum of terms is: {sum}")



#Q-10. series of (x-x^3+x^5-....)

import math

sum=0
term=0
x = int(input("Input the value of x : "))
n = int(input("Input the number of terms : "))
for i in range(1,n+1):
    #term=(math.pow(-1,i-1))*(math.pow(x,(2*i-1)))
    term=((-1)**(i-1))*(x**((2*i)-1))
    sum=sum+term
    print(math.trunc(term))
   
print(f"sum of terms is: {round(sum)}")










