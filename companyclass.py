def liststring(lst):
    str1=""
    for i in lst:
        str1=i+" "+str1
    return str1

class Company:
    def __init__(self,name="",email=""):
        self.__name=name
        self.__email=email
    
    def __str__(self):
        return f"""
    Name: {self.__name} 
    Email: {self.__email} """

class Vendor(Company):
    vcount=0
    def __init__(self,name="",email="",products=[]):
        Vendor.vcount=Vendor.vcount+1
        super().__init__(name,email)
        self.__vid="VID"+ str(Vendor.vcount)
        self.__products=products
    
    def __str__(self):
        return f"""
    Vendor ID: {self.__vid} """+super().__str__()+f"""
    Products: {liststring(self.__products)} """

class Customer(Company):
    custcount=0
    def __init__(self,name="",email="",crecl="",disc=0,plan=""):
        Customer.custcount=Customer.custcount+1
        super().__init__(name,email)
        self.__custid="CID"+ str(Customer.custcount)
        self.__crecl=crecl
        self.__disc=disc
        self.__plan=plan
    
    def __str__(self):
        return f"""
    Customer ID: {self.__custid}"""+super().__str__()+f"""
    Credit Class: {self.__crecl} 
    Discounts: {self.__disc}
    Plan: {self.__plan}"""

class IndividualCust(Customer):
    def __init__(self,name="",email="",crecl="",disc=0,plan="",pnumber=""):
        super().__init__(name,email,crecl,disc,plan)
        self.__pnumber=pnumber
        
    def __str__(self):
        return super().__str__()+f"""
    Phone Number: {self.__pnumber}"""

class CompanyCust(Customer):
    def __init__(self,name="",email="",crecl="",disc=0,plan="",rmanager="",creln="",ext="", lstnumber=[]):
        super().__init__(name,email,crecl,disc,plan)
        self.__rmanager=rmanager
        self.__creln=creln
        self.__ext=ext
        self.__lstnumber=lstnumber
        
    def __str__(self):
        return super().__str__()+f"""
    Relationship Manager: {self.__rmanager}
    Credit Line: {self.__creln}
    Extension: {self.__ext}
    List of Number: {liststring(self.__lstnumber)}"""

if __name__=="__main__":
    v1=Vendor("Nirav","nirav@",["screw","file","nozzle"])
    print(v1)
        
                
        
        

    



















