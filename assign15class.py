###File Handling


from abc import abstractmethod,ABC

class Person:
    def __init__(self,pid=0,name=""):
        self.__pid=pid
        self.__name=name
    
    def get__pid(self):
        return self.__pid
    def get__name(self):
        return self.__name
       
    def set_pid(self,pid):
        self.__pid = pid
    def set_name(self,name):
        self.__name = name
    
    def __str__(self):
        return f"{self.__pid},{self.__name},"
    
class Employee(Person,ABC):
    def __init__(self,pid=0,name="",dept="",desg=""):
        super().__init__(pid,name)
        self.__dept=dept
        self.__desg=desg
   
    @abstractmethod
    def calculateSal(self):
        pass
    
    @abstractmethod
    def objecttostring(self):
        pass
    
    def __str__(self):
        return super().__str__()+f"{self.__dept},{self.__desg},"

class Salariedemp(Employee):
    def __init__(self,pid=0,name="",dept="",desg="",sal=0):
        super().__init__(pid,name,dept,desg)
        self.__sal=sal

    def get__sal(self):
        return self.__sal
       
    def set__sal(self,sal):
        self.__sal = sal
        
    def calculateSal(self):
        return (self.__sal)+0.10*(self.__sal)+0.15*(self.__sal)-0.08*(self.__sal)
    
    def objecttostring(self):
        return super().__str__()+f"{self.__sal}\n"
        
    def __str__(self):
        return super().__str__()+f"{self.__sal}"
    
class Contract(Employee):
    def __init__(self,pid=0,name="",dept="",desg="",hr=0,charge=0):
        super().__init__(pid,name,dept,desg)
        self.__hr=hr
        self.__charge=charge
    
    def get_name(self):
        return self.__name
    def get_name(self):
        return self.__name
       
    def set_pid(self,pid):
        self.__pid = pid   
    def set_pid(self,pid):
        self.__pid = pid
    
    def calculateSal(self):
        return (self.__hr)*(self.__charge)
    
    def objecttostring(self):
        return super().__str__()+f"{self.__hr},{self.__charge}\n"
    
    def __str__(self):
        return super().__str__()+f"{self.__hr},{self.__charge}"
    
if __name__=="__main__":
    
    s1=Salariedemp("Nirav","IT","Data Scientist", 150000)
    c1=Contract("Yash","AI","Data Engineer", 175, 1000)
    
    print(s1)
    print(s1.calculateSal())
    
    print(c1)
    print(c1.calculateSal())
    
