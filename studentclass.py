class Student:
    count=0
    def __init__(self,name="",m1=0,m2=0,m3=0):
        Student.count=Student.count+1
        self.__sid="STD" + str(Student.count)
        self.__name=name
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
        
    def get_sid(self):
        return self.__sid
    def get_name(self):
        return self.__name
    
    def gpaCalculation(self):
        return (1/3)*(self.__m1)+(1/2)*(self.__m2)+(1/4)*(self.__m3)
        
    def __str__(self):
        return f"""
Student Details:
_________________________________
Student Id: {self.__sid}
Student Name: {self.__name}
M1: {self.__m1}
M2: {self.__m2}
M2: {self.__m3}"""
        
if __name__=="__main__":
    
    S1=Student("Harsh",90,89,99)
    print(S1)
    S2=Student("Nirav", 99,99,99)
    print(S2)
    
    print(S1.gpaCalculation())
    
    
    









