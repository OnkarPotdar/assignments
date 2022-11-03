#Q-1. accept lines from user and store in a list.
'''
convert list into dictionary
store all lines ending with m or mid in a list and assign list to key “found” in dictionary
otherwise store it in a list and assign it to key not found
'''

import re

dict1={"found":[],
       "notfound":[]}

ans="y"

while ans=="y" or ans=="Y":
    
    s=input("Enter the string: ")
    
    m=re.search("m+i?d?$",s,re.I)
    
    if m!=None:
        dict1["found"].append(s)
        
    else:
        dict1["notfound"].append(s)
    
    ans=input("Do you want to continue (y/n):")

for key,values in dict1.items():
    print(f"{key}---->\n {values}")


#Q-2. accept strings in following format from user and store it in a list:
'''
12, queen, 2018, kangana, 1234562018, pune
15, dangal, 2018, aamir, 34562562018, mumbai
12, sholay, 1995, amitabh, 7869272018, pune
---- Display movie name and year separated by, if the movie was released in 2018.
---- Display movies released in pune city.
'''

#s= "15, RRR, 2018, aamir, 34562562018, mumbai"

list1=[]
list2=[]

ans="y"

while ans=="y" or ans=="Y":
        
    s=input("Enter the string: ")
   
    m=re.search("\d{4}",s,flags=re.I)
    
    if m!=None:
        #print("pattern Found")
        year=m.group()
        
        if year == '2018':
            
            n=re.search("[A-Za-z]{1,}",s,flags=re.I)
            temp1=""
    
            if n!=None:
                movie=n.group()
                temp1=movie+"-"+year
            list1.append(temp1)
    
    else:
        print("pattern not Found")
    
    n=re.search("\w+$",s,flags=re.I)
    
    if n!=None:
        #print("pattern Found")
        city=n.group()
        
        if city == 'pune':
            
            n=re.search("[A-Za-z]{1,}",s,flags=re.I)
            temp2=""
    
            if n!=None:
                movie=n.group()
                temp2=movie+"-"+city
            list2.append(temp2)
    
    else:
        print("pattern not Found")
    
    ans=input("Do you wnat to add more?(y/n): ")
    
print(list1)
print(list2)

#Q-3. Accept 2 patterns from user
'''Accept multiple strings from user till user enters end, if string has pattern 1 then store it
in list1
If it has pattern 2 then store it in list2 else display message pattern not found
'''

pat1=input("Enter the first pattern to search: ")
pat2=input("Enter the second pattern to search: ")

linein=[]
lne=''
while lne!= 'end':
    lne=input('Enter a string: ')
    linein.append(lne)
linein.pop()
print("Input String is: " ,linein)
forp1=[]
forp2=[]
for li in linein:
    m=re.search(pat1,li,re.I)
    if m!=None:
        forp1.append(li)
    
    elif re.search(pat2,li,re.I)!=None:
        forp2.append(li)
    else:
        print("Neither pattern found in string")
print("First list with pattern 1 is: ",forp1)
print("Second list with pattern 2 is: ",forp2)































