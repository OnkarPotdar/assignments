#Assignment 03 - String

#Q-1.

str1= "RakeshzipPetabb"

str2= "JazzbonAyzz"

len1=len(str1)
len2=len(str2)

l1=len1//2
l2=len2//2

print(str1[(l1-1):(l1+2)])

print(str2[(l2-1):(l2+2)])



#Q-2.
s1="Ault"
s2="Kelly"

l1=len(s1)
l2=len(s2)

s3=s1[:l1//2]+s2+s1[l1//2:]

print(s3)


#Q-3.

def mix_string(s1,s2):

    l1=len(s1)
    l2=len(s2)

    first_ch=s1[:1]+s2[:1]

    middle_ch=s1[(l1//2):((l1//2)+1)]+s2[(l2//2):((l2//2)+1)]

    last_ch=s1[(l1-1):]+s2[(l2-1):]

    mix_string=first_ch+middle_ch+last_ch

    return mix_string

s1="America"
s2="Japan"

print(mix_string(s1,s2))



#Q-4. Condition 01

s1 = 'PytHONStudy'
s2=[]
s3=[]
for char in s1:
    if char.islower():
        s2.append(char)
    else:
        s3.append(char)

s4=''.join(s2+s3)
print(s4)


#Q-4. Condition 02

s1 = 'PytHONStudy'
for char in s1:
    if char.islower():
        print(char,end="")
for char in s1:
    if char.isupper():
        print(char,end="")

#Q-5. Type 01

s1="abc"
s2="xyz"
s3=[]
s4=[]
l1=len(s1)
l2=len(s2)
m=0
n=l2-1
for i in range(len(s1)):
    p1=s1[m]
    p2=s2[n]
    s3.append(p1+p2)
    m=m+1
    n=n-1
s4= ''.join(s3)
print(s4)

#Q-5. Type 02

s1="abcdefgh"
s2="stuvwxyz"
s3=""
lst2=list(s2)

s1.add(s2)
print(s1)
lst2.reverse()
s2=str(lst2)

print(''.join(s2))


#Q-6.

s1="Welcome to USA. usa awesome, isn't it?"

pos=s1.rfind("usa")

while pos!=-1:
    print(pos)
    pos=s1.rfind("usa" or "USA",0,pos+1)
    

