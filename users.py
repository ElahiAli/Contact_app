import csv
import imp
from contact import create,update,delete,search,read
import os.path

registered_user = [] 

class Users:
    def __init__(self,username,password,email,birthday,birthmonth,birthyear):
        self.username = username
        self.password = password
        self.email = email
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear
        
        with open('users.csv',mode='a',newline='') as csvfile:
            csv_writer = csv.writer(csvfile,delimiter=',' )
            csv_writer.writerow([username,password,email,birthday,birthmonth,birthyear])
            

def register(username):
        password = input("Please enter pass: ")
        password2 = input("Please re-type passwoed: ")
        email = input("enter your email: ")
        birthday = input("enter your birthday: ")
        birthmonth = input("enter your birthmonth: ")
        birthyear = input("enter your birthyear: ")
        if password2 == password:
            Users(username,password,email,birthday,birthmonth,birthyear)
            print("Rgistration is succesfull!")
            
    
def login():
    with open('users.csv', mode='r', newline='') as csvfile:
        username = input("enter your username: ")
        password = input("Please enter password: ")
        csv_reader = csv.reader(csvfile,delimiter=',' )
        for row in csv_reader:
                if row[:2] == [username,password]:
                    print('you are logged in!')
                    return True
    print("Please try again!")
    return False    


def first_option(username):
    print("1.Login\n2.exit")
    option = input("Please select: ")
    if option == '1':
        print("Please login: ")
        if login() == True:
            print("-------------------")
            admin(username)
        else:
            print("-------------------")
            first_option(username)
    elif option == '2':
        exit()
    else:
        print("try again")
        first_option(username)


def admin(username):
    print("1.Display all contacts")
    print("2.Admin pannel")
    print("press 'q' to Loging out")
    ask = input("Please select: ")
    if ask == '1':
        print("-------------------")
        print("*Contact info*")
        read(username)
        print("-------------------")
        admin(username)
    elif ask == '2':
        print("-------------------")
        print("***admin pannel***")
        print("1.create\n2.update\n3.search\n4.delete")
        print("press 'q' to Quit")
        admim_ask = input("Please select: ")
        if admim_ask == '1':
            print("-------------------")
            print("creating contact")
            create(username)
            print("-------------------")
            admin(username)
        elif admim_ask == '2':
            print("-------------------")
            print("updating contact")
            update(username)
            print("-------------------")
            admin(username)
        elif admim_ask == '3':
            print("-------------------")
            print("searching contact")
            search(username)
            print("-------------------")
            admin(username)
        elif admim_ask == '4':
            print("-------------------")
            print("deleting contact")
            delete(username)
            print("-------------------")
            admin(username)
        elif admim_ask == 'q':
            print("exiting... ")
            print("-------------------")
            admin(username)
        else:
            print("-------------------")
            admin(username)
    elif ask == 'q':
        print("Loging out...")
        print("-------------------")
        first_option(username)
    else:
        print("-------------------")
        admin(username)


def main():
    file_exists = os.path.exists("users.csv")
    if file_exists:
        with open('users.csv','r') as csvfile:
            reader = csv.reader(csvfile,delimiter=',' )
            for row in reader:
                registered_user.append(row)
    print("-------------------------------------------------------")  
    print("***welcom to contact app***")
    username = input("what's your username? ")
    ask = input("Did you registered your name? 1 = YES | 2 = NO | q = Quit: ") 
    
    if ask == '1':
        for row in registered_user:
            if row[0] == username:
                print("you are registered")
                first_option(username)
        else:
            register(username)
            print("-------------------")
            first_option(username)
                    
    elif ask == '2':
        for row in registered_user:
            if row[0] == username:
                print("you are registered")
                print("-------------------")
                first_option(username)
        else:
            register(username)
            print("-------------------")
            first_option(username)

    elif ask == 'q':
        exit()



if __name__=="__main__":
    main()

