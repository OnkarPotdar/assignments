# Assignment 6 - Tuple
#Q-1

aTuple = (10,20,30,40,50,60)
lst = list(aTuple)
lst.reverse()
tpl = tuple(lst)
print(tpl)

#Q-2

aTuple = ("Orange",[10,20,30],(5,15,25))
print(aTuple[1][1])

#Q-3

aTuple =  (10,20,30,40)
a,b,c,d=aTuple
print(f"{a}---{b}---{c}---{d}")

#Q-4

tuple1 = (11,22)
tuple2 = (99,88)
tuple1,tuple2 = tuple2,tuple1
print(tuple1)
print(tuple2)

#Q-5

tuple1 = (11,22,33,55,44,66)
a = tuple1.index(44)
b = tuple1.index(55)
tuple2=tuple1[a],tuple1[b]
print(tuple2)

#Q-6
tuple1 = (11,[22,33],44,55)
tuple1[1][0]=200
print(tuple1)