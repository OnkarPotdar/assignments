
class Friends:
    count=0
    def __init__(self,name="",lastname="",hobbies=[],mobno="",email="",bdate="",address=""):
        Friends.count+=1
        self.__fid = Friends.count
        self.__name = name
        self.__lastname = lastname
        self.__hobbies = hobbies
        self.__mobno = mobno
        self.__email = email
        self.__bdate = bdate
        self.__address = address
        
    def get_fid(self):
        return self.__fid
    def get_name(self):
        return self.__name
    def get_lastname(self):
        return self.__lastname
    def get_hobbies(self):
        return self.__hobbies
        
    def __str__(self):
        return f"""
    Friend list
    =================================
    Friend Id : {self.__fid}
    Name : {self.__name}
    Lastname : {self.__lastname}
    Hobbies : {self.__hobbies}
    Mobile no : {self.__mobno}
    Email : {self.__email}
    Birthday : {self.__bdate}
    Address : {self.__address}"""


if __name__ =="__main__":
    f = Friends('Harsh',"Parmar",['play','travel'],1234567898,'harsh@','240900','Surat')
    print(f)
    