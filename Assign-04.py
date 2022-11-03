# Assignment 04 - Set

#Q-1.

sampleset={"Yellow","Orange","Black"}
samplelist=["Blue","Green","Red","Yellow","Orange"]

#set1=sampleset.union(set(samplelist))

set1=sampleset|(set(samplelist))

print(set1)


#Q-2.

set1={"10","20","30","40","50"}
set2={"30","40","50","60","70"}
print(set1&set2)


#Q-3.

set1={10,20,30,40,50,25}
set2 = {30,40,50,60,70,100}
print(set1.symmetric_difference(set2))


#Q-4.

set1={10,20,30,40,50}
set2={30,40,50,60,70}
print("Intersection --> ",set1.intersection(set2))
print("difference --> ",set1.difference(set2))
print("union --> ",set1.union(set2))
print("symmetric_difference --> ",set1.symmetric_difference(set2))
print("difference_update --> ",set1.difference_update(set2))
print(set1)
print("symmetric_difference_update --> ",set1.symmetric_difference_update(set2))
print(set1)

#Q-5.

set1={10,20,30,80,150,115}
set2={55,60,50,60,70,75,81,89}
list1=[]

avg=0
sum=0
len1=len(set1)
for i in set1:
    sum=sum+i
avg=sum/len1

for i in set2:
    if i>=avg:
        set1.add(i)
print(set1)

#Q-6.

size = int(input("Enter size of the string: "))
ans = 'n'
set1=set()
while ans != 'y':
    ans = input("Enter the string: ")
    strlen=len(ans)
    if strlen>size:
        set1.add(ans)
    ans=input("Exit (y/n)?")
print(set1)
