import csv

class Contact:
    def __init__(self,user,name,lastname,phonenumber):
        self.user = user
        self.name = name
        self.lastname = lastname
        self.phonenumber = phonenumber

        with open('contact.csv',mode='a',newline='') as csvfile:
            csv_writer = csv.writer(csvfile,delimiter=',' )
            csv_writer.writerow([user,name,lastname,phonenumber])
            

def create(user):
    name = input("Please enter contact name: ")
    lastname = input("Please enter contact lastname: ")
    phonenumber = input("Please enter phonenumber: ")
    Contact(user,name,lastname,phonenumber)
    print("contact saved.")
    return True
    

def update(user):
    contact_list = []
    with open('contact.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for data in reader:
            contact_list.append(data)
        

    with open('contact.csv','w+') as csvfile:
        writer = csv.writer(csvfile,delimiter=',' )
        name = input("Please enter contact name: ")
        for row in contact_list:
            if row[1] == name:
                if row[0] == user:
                    print(f"name : {row[1]} -- lastname : {row[2]} -- phonenumber : {row[3]}")
                    name = input("Please enter new-contact name: ")
                    lastname = input("Please enter new-contact lastname: ")
                    phonenumber = input("Please enter new-phonenumber: ")

                    row[1] = name
                    row[2] = lastname
                    row[3] = phonenumber
                    for info in contact_list:
                        writer.writerow(info)
                    print("contact updated.")
        else:              
            with open('contact.csv','w') as csvfile:
                writer = csv.writer(csvfile,delimiter=',' )
                for info in contact_list:
                    writer.writerow(info)
                
            
def delete(user):
    contact_list = []
    with open('contact.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',' )
        for data in reader:
            contact_list.append(data) 
    
    with open('contact.csv','w+',) as csvfile:
        writer = csv.writer(csvfile,delimiter=',' ,lineterminator='\n')
        name = input("Please enter contact name: ")
        for row in contact_list:
            if row[1] == name:
                if row[0] == user:
                    print(f"name : {row[1]} -- lastname : {row[2]} -- phonenumber : {row[3]}")
                    print(f"contact {name} Deleted.")
                    continue       
            writer.writerow(row)     
                    
                    
def search(user):
    with open('contact.csv', mode='r', newline='') as csvfile:
        name = input("Please enter contact name: ")
        lastname = input("Please enter contact lastname: ")
        csv_reader = csv.reader(csvfile,delimiter=',' )
        for row in csv_reader:
                if row[:3] == [user,name,lastname]:
                    print(f"name : {row[1]} | lastname : {row[2]} | phonenumber : {row[3]}")
                    print("contact found.")
                    return True
    print("Please try again!")
    return False    


def read(user):
    with open('contact.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',' )
        for row in reader:
            if row[0] == user:
                print(row)





