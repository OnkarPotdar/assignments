from friendclass import *
friendlist = []
namelist = []
hobbyset=set()
hobbydict=dict()

def addFriend():
    name = input('Enter name: ')
    lastname = 'surti'
    hobbieslist = []
    ans = "y"
    while ans == 'y':
        hobby = input('Enter hobby: ')
        hobbieslist.append(hobby)
        ans = input("Continue? ")
    mobno = "123"
    email = "abc@"
    bdate = "01012020"
    address = "SURAT"
    f = Friends(name,lastname,hobbieslist,mobno,email,bdate,address)
    friendlist.append(f)

def displayAll():
    for friend in friendlist:
        print(friend)
        
def searchbyid(fid):
    for friend in friendlist:
        if friend.get_fid() == fid:
            return friend
    else:
        return None
    
def searchbyname(fname):
    for friend in friendlist:
        if friend.get_name() == fname:
            namelist.append(friend)
    return namelist

def hobbywisename(hb):
    newlst=[]
    for st in friendlist:
        if hb in st.get_hobbies():
            newlst.append(st.get_name()+" "+st.get_lastname())
    return newlst
        
choice = 0

while choice != 6:
    choice = int(input("""
1. Add Friend
2. Display All Friend
3. Search by id
4. Search by name
5. Display all friend with a particular hobby
6. Exit
Choice: """))

    match choice:
        case 1:
            addFriend()
        
        case 2:
            displayAll()
        
        case 3:
            fid = int(input('Enter friend id for search: '))
            status = searchbyid(fid)
            if status != None:
                print(status)
            else:
                print('Friend Id not found')
        
        case 4:
            fname = input('Enter friend name for search: ')
            namelist = searchbyname(fname)
            if len(namelist) > 0:
                for name in namelist:
                    print(name)
            else:
                print('Name not found')
        
        case 5:
            hobby = input('Enter hobby for search: ')
            lst = hobbywisename(hobby)
            
            print(f"Hobby: {hobby} \n\nFriend Name:\n")
            if len(lst)>0:
                for i in lst:
                    print(i)
            else:
                print('Hobby not found..')
                    
        case 6:
            print("Thanks for visiting....")
        
        case _:
            print("Wrong choice....")







