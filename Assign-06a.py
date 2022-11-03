#Assignment 06 - Lists

#Q-1.

alist=[100,200,300,400,500]
rlist=[]
length=len(alist)

for i in range(length):
    rev=alist.pop()
    rlist.append(rev)

print(rlist)



#Q-2.

list1=["M","na","i","Raj"]
list2=["y","me","s","esh"]
list3=[]

for ch1,ch2 in zip(list1,list2):
    list3.append(ch1+ch2)

print(list3)



#Q-3.

alist=[1,2,3,4,5,6,7]
sqr=[]

for i in alist:
    sqr.append(i*i)

print(sqr)



#Q-4.

list1=["Hello","Welcome"]
list2=["Students","Sir"]
list3=[]

for ch1 in list1:
    for ch2 in list2:
        list3.append(ch1+" "+ch2)

print(list3)



#Q-5.

list1=[10,20,30,40]
list2=[100,200,300,400]
len2=len(list2)

rlist2=[]
for i in range(len2):
    rev=list2.pop()
    rlist2.append(rev)

for ch1,ch2 in zip(list1,rlist2):
    print(f"{ch1} {ch2}")



#Q-6.

str=""
list1=["Ashish","","Atharva","Amit","","Revati"]
for char in list1:
    if str in list1:
        list1.remove(str)
print(list1)



#Q-7.

list1=[10,20,[300,400,[5000,6000],500],30,40]

list1[2][2].append(7000)

print(list1)


#Q-8.

list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sublist=["h","i","j"]

list1[2][1][2].extend(sublist)

print(list1)

#Q-9.

list1=[5,10,15,20,25,50,20]

pos=list1.index(20)

list1[pos]=200

print(list1)

#Q-10.

list1=[5,20,15,20,25,50,20]
#list1.reverse()

print(list1)
for i in list1:
    if i==20:
        list1.remove(20)

print(list1)