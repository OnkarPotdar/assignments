# Assignment 05 Dictionary

#Q-1. Convert lists to dictionary.

keys=["ten","twenty","thirty"]
values=[10,20,30]
dict1={}

for i,j in zip(keys,values):
    dict1[i]=j

print(dict1)


#Q-2. Merge following dictionary.

dict1={'ten': 10, 'twenty': 20, 'thirty': 30}
dict2={'thirty': 30, 'forty': 40, 'fifty': 50}
dict3={}

dict3={**dict1,**dict2}
print(dict3)


#Q-3. Value of Key.

sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,
                                                         "history":80}}}}
print(sampleDict["class"]["student"]["marks"]["history"])


#Q-4. Remove key.

sampledict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}

keystoremove = ["name", "salary"]

for i in keystoremove:
    sampledict.pop(i)

print(sampledict)

#Q-5.display all the keys with value 200 from the following dictionary

sampleDict = {'a': 100, 'b': 200, 'c': 300,'d':200}
ansDict = {}
for key,value in sampleDict.items():
    if value == 200:
        ansDict[key]=value
print(ansDict)


#Q-6. Rename key 'city' to 'location'

sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"}

sampleDict.pop("city")

secondDict = {"location":"New York"}
sampleDict.update(secondDict)

print(sampleDict)


#Q-7. display the key of a maximum value

sampleDict = {'Physics': 82,'Math': 65,'history': 75}

max=0
key1=""

for keys,values in sampleDict.items():
    if max<values:
        max=values
        key1=keys
else:
    print(f"{key1} -> {max}")

#Q-8. Accept name and new salary for a employee, modify salary.

sampleDict = {'emp1': {'name': 'Jhon', 'salary': 7500},
            'emp2': {'name': 'Emma', 'salary': 8000},
            'emp3': {'name': 'Brad', 'salary': 6500}}

entername=input("Enter name: ")
new_salary=int(input("Enter new salary for Employee: "))

for key,value in sampleDict.items():
    if value["name"]==entername:
        if entername in value.values():
            if value['salary'] > new_salary:
                print("Wrong salary")
                break
            else:
                value['salary']=new_salary
                print("Salary modified sucessfully.")
                break
else:
    print(f"{entername} not found. ")
    
print(sampleDict)

            
'''
else:
    sampleDict[entername]['salary'] = new_salary
    print("Salary modified successfully")
    print(sampleDict)
'''
