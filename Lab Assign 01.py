# Lab Assignment 1

#Q-1. Print a Calender.
# monthdays = 31 and startday = 3 (i.e. Thus)

monthday=int(input("Enter the days in a month: "))
startday=int(input("""Enter the starting day:
(i.e. 0=Mon,1=Tue,2=Wed,3=Thus,4=Fri,5=Sat,6=Sun): """))

print("Mon\tTue\tWed\tThus\tFri\tSat\tSun")

for space in range(startday):
    print("",end="\t")

for date in range(1,monthday+1):

    print(f"{date}",end="\t")

    if (date+startday)%7==0:
        print()
print("\nThank you for Using Program...!!!")

#Q-2. Histogram.

list1=[]
listinput=int(input("Enter total numbers to add in list: "))

for i in range(1,listinput+1):
    num=int(input(f"Enter number {i} to add in list: "))    
    list1.append(num)

print(f"\nEnter list is: {list1}\n")

print("Histogram for above list is as below:\n")

for i in list1:
    print("*"*i)

print("\nThank you for Using Program...!!!")

 
#Q-3. Check the Palindrome. CONDITION - 01

rawstring=input("Enter string to check Palindrome: ")
lowerstring=rawstring.lower()
alnumstring=""
reversestring=""

for letter in lowerstring:
    if letter.isalnum():
        alnumstring=alnumstring+letter

for letter in alnumstring:
    reversestring=letter+reversestring

if alnumstring==reversestring:
    print("\nThe string is Palindrome...!!!")
else:
    print("\nThe string is NOT Palindrome...!!!")

print("\nThank you for Using Program...!!!")

# OR CONDITION - 02

alpha=""
rev=""
for i in lowerstring:
    if i.isalpha():
        alpha=alpha+i
rev=alpha[::-1]
rev
if rev==alpha:
    print("true")
else:
    print("false")
   
#Q-4. Check the Pangram.

rawstring=input("Enter string to check Pangram: ")
lowerstring=rawstring.lower()
alphastring=""
pangramset=set()

for letter in lowerstring:
    if letter.isalpha():
        alphastring=alphastring+letter

pangramset=set(alphastring)

if len(pangramset)==26:
    print("\nThe string is Pangram...!!!")
else:
    print("\nThe string is NOT Pangram...!!!")

print("\nThank you for Using Program...!!!")

#Q-5. cryptography, a Caesar cipher ROT-13 ("rotate by 13 places")
#Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!

cipherset={'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
           'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
           'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
           'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R','F':'S',
           'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
           'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F','T':'G', 'U':'H', 'V':'I',
           'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

encodedstring=input("Enter string for Caesar cipher ROT-13: ")

decodedstring=""

for ch in encodedstring:
    for key, values in cipherset.items():
        if ch.isalpha():
            if key==ch:
                decodedstring=decodedstring+values
        else:
            decodedstring=decodedstring+ch
            break

print(decodedstring)

#Q-6. Given a dictionary of students and their favourite colours:
#people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
#1. Find out how many students are in the list
#2. Change Lisa’s favourite colour
#3. Remove 'Jenny' and her favourite colour
#4. Sort and print students and their favourite colours alphabetically by name

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

print("1. Find out how many students are in the list...")

print(f"\tNumber of students in the list: {len(people)}")

print("\n2. Change Lisa’s favourite colour...")

lisacolour=input("\tEnter Lisas new favourite colour: ")

people['Lisa']=lisacolour

print("\n\tLisa’s new favourite colour is:\n")

for key,value in people.items():
    if key=='Lisa':
        print(f"\t{key} ---> {value}")
print("\n3. Remove 'Jenny' and her favourite colour...")
people.pop('Jenny')
for key,value in people.items():
    print(f"\t{key} ---> {value}")

print("\n4. Sort and print students and their favourite colours alphabetically by name")
list1=[]
list1=list(people)
list1.sort()
dict1=dict.fromkeys(list1)
dict3={**dict1,**people}
print(f"Sort and print: {dict3}")


#Q-7. function translate() that will translate a text
#(Swedish for "robber's language")

def translate(rawstring):
    outputstring=""
    vowellist=['a','e','i','o','u','A','E','I','O','U']
    for ch in rawstring:
        if ch.isalpha():
            if ch not in vowellist:
                outputstring = outputstring + ch + "o" + ch
            else:
                outputstring = outputstring + ch
        else:
            outputstring = outputstring + ch
    return outputstring

rawstring=input("Enter String to Translate: ")
outputstring = translate(rawstring)
print(outputstring)


#Q-8. The function should return n! (n factorial)

#function to count and print factor
def factorfunction(number):
    factor=1
    for i in range(1,number+1):
        factor=factor*i
    return factor

number=int(input("Enter the number:"))

for i in range(1,number+1):

    factor=factorfunction(i)
    print(f"{i}\t{factor}")


#Q-9. Write a recursive sum from 1 to x

#recursion sum function for addition:
def recursionsum(x):
    if x==0:
        return x
    return x+recursionsum(x-1)

x=int(input("Enter the Value: "))

totalsum=recursionsum(x)
for i in range(1,x+1):
    print(f"{i}+",end="")
print(f"\nSum of input is sum({x})={totalsum}")


#Q-10. Define a function overlapping()

#function overlapping to be check

def overlapping(lst1,lst2):

    set_lst1={}
    set_lst2={}
    set_overlap={}
    set_lst1=set(lst1)
    set_lst2=set(lst2)
    set_overlap=(set_lst1)&(set_lst2)
    
    if len(set_overlap)>0:
        return True
    else:
        return False

number=int(input("Enter number to add in list: "))
lst1=[]
lst2=[]

str=""

for i in range(number):
    str=input(f"Enter List1[{i+1}]= ")
    lst1.append(str)
    str=input(f"Enter List2[{i+1}]= ")
    lst2.append(str)

status=overlapping(lst1,lst2)
if status:
    print(f"{status}...!!!")
else:
    print(f"{status}...!!!")

    
#Q-11. Write a function find_longest_word() that takes a list of words and
#returns the length.

#function to check longest word
def find_longest_word(lst):
    length=0
    word=""
    for i in lst:
        if length<len(i):
            length=len(i)
            word=i
    return length,word

number=int(input("Enter number to add in list: "))
lst=[]

str=""

for i in range(number):
    str=input(f"Enter List[{i+1}]= ")
    lst.append(str)

length,word=find_longest_word(lst)
print(f"\n Longest word is {word} and length is {length}...!!!")
    
#Q-12. Write a function filter_long_words() that takes a list of words
#      and an integer.

#function to filer words longer then integer
def find_longest_word(lst,integer):
    length=[]
    word=[]
    for i in lst:
        if integer<=len(i):
            length.append(len(i))
            word.append(i)
    return length,word

number=int(input("Enter number to add in list: "))
integer=int(input("Enter minimum size of word: "))
lst=[]

str=""

for i in range(number):
    str=input(f"Enter List[{i+1}]= ")
    lst.append(str)

length,word=find_longest_word(lst,integer)

for i,j in zip(word,length):
    print(f"Word: {i}, Length: {j}")

#Q-13. Define a simple "spelling correction" function correct() that takes a
#      string and sees to it that
#      1) two or more occurrences of the space character is compressed into
#      one, and 2) inserts an extra space after a period if the period is
#      directly followed by a letter.

#spelling corrction for blank and after period

import re
 
def correct(rawstring):
 
    #Removing extra spaces
    correctedstring = re.sub('\ +',' ',rawstring)
 
    #Putting extra space after period
    correctedstring = re.sub('\.','. ',correctedstring)
 
    print(correctedstring)
 
rawstring=input("Enter String for spelling correction: ") 
correct(rawstring)

#Q-14. In English, present participle is formed by adding suffix -ing to 
# infinite form: go -> going. A simple set of heuristic rules can be given 
# as follows: 
# If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, 
# knee, etc.) 
# If the verb ends in ie, change ie to y and add ing 
# For words consisting of consonant-vowel-consonant, double the final letter
# before adding ing 
# By default just add ing
# Your task in this exercise is to define a function make_ing_form() which 
# given a verb in infinitive form returns its present participle form. Test 
#your function with words such as lie, see, move and hug.

#to check vowel or not
def checkvowel(c):
    if c in ["a","e","i","o","u"]:
        return True
    else:
        return False


#function to change verb to ing form
def make_ing_form(rawstring):
    ch=""
    if rawstring.endswith("ie"):
        ch=rawstring.removesuffix("ie")
        rawstring=ch+"y"+"ing"
        return rawstring
    elif rawstring.endswith("e"):
        ch=rawstring.removesuffix("e")
        rawstring=ch+"ing"
        return rawstring
    elif (not checkvowel(rawstring[-3])) and (checkvowel(rawstring[-2])) and (not checkvowel(rawstring[-1])):
        rawstring=rawstring+rawstring[-1]+"ing"
        return rawstring
    else:
        return rawstring+"ing"
    
rawstring=input("Enter the verb: ")
status=make_ing_form(rawstring)
print(f"{rawstring} is changed to {status}.")
