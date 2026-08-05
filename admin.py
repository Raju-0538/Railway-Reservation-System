import csv
import os
from user import User


fields = ['train_number','train_name','source','destination','price','available_seats','seat_numbers']
class Admin(User):
    def __init__(self,email,password):
        self.email = email
        self.password = password
    def register(self,name):
        self.name = name
        if os.path.exists('Admin.csv'):
            with open('Admin.csv','r',newline="") as file:
                read = csv.DictReader(file)
                for admin in read:
                    if self.email == admin['email']:
                        return "User Already Exists !"
        with open('Admin.csv','a+',newline="") as file:
            admin = {}
            fields = ['email','Name','Password']
            admin[self.email] = {
                'Name' : self.name,
                'Password' : self.password
            }
            write = csv.DictWriter(file,fieldnames=fields)
            if file.tell() == 0:
                write.writeheader()
            for email,details in admin.items():
                write.writerow({
                    'email' : email,
                    'Name' : details['Name'],
                    'Password' : details['Password']

                })
                
        return "Registered Successfully !"
    def login(self):
        with open('Admin.csv','r',newline="") as file:
            read = csv.DictReader(file)
            for row in read:
                if row['email'] == self.email:
                    if row['Password'] == self.password:
                        return "Login Successfull !"
                    
            return "Invalid Email or password !" 
    def AddTrain(self,train_number:int,train_name:str,source:str,destination:str,price:int,available_seats:int,seat_numbers:list):
            with open('Train.csv','r',newline="") as file:
                read = csv.DictReader(file)
                for row in read:
                    if row['train_number'] == str(train_number):
                        return "Train Number already Exists !"
                with open('Train.csv','a',newline="") as f:
                    write = csv.DictWriter(f,fieldnames=fields)
                    if file.tell() == 0:
                        write.writeheader()
                    write.writerow({
                        'train_number' : train_number,
                        'train_name' : train_name,
                        'source' : source,
                        'destination' : destination,
                        'price':price,
                        'available_seats' : int(available_seats),
                        'seat_numbers' : list(seat_numbers)
                    })
                return "Added Successfully !"
    def ViewAllUsers(self):
        if not os.path.exists('User.csv') :
            return "There is no users !"
        with open('User.csv','r') as file:
            read = csv.DictReader(file)
            print('-'*20,'ALL UESRS','-'*20)
            for row in read:
                print(f"User Name : {row['Name']}")
                print(f"Email : {row['email']}")
                print(f"Password : {row['Password']}")
                print('*'*50)
            print('-'*20,'THE END','-'*20)
    def ViewAllBookedTickets(self):
        if not os.path.exists('Booked_Tickets.csv'):
            return "There is No Tickets Booked !"
        with open('Booked_Tickets.csv','r') as file:
            read = csv.DictReader(file)
            print('-'*20,'BOOKED TICKETS','-'*20)
            for row in read:
                print(f"User Email : {row['User_email']}")
                print(f"Train Number : {row['train_number']}")
                print(f"No of Tickets Booked : {row['Booked_seats']}")
                print(f"Booked Seat Numbers : {row['seat_numbers']}")
                print('*'*50)
            print('-'*20,'THE END','-'*20)

    def DeleteTrain(self,train_number):
        if not os.path.exists('Train.csv'):
            return "There is no trains available to delete !"
        with open('Train.csv','r') as file:
            read = csv.DictReader(file)
            lst = list(read)
            flag = 0
            for row in range(len(lst)):
                
                if lst[row]['train_number'] == str(train_number):
                    flag += 1
                    lst.pop(row)
                    break
            if flag == 0:
                return "Train Not Found !"
            with open('Train.csv','w',newline="") as f1:
                write = csv.DictWriter(f1,fieldnames=fields)
                write.writeheader()
                for row in lst:
                    write.writerow({
                        'train_number':row['train_number'],
                        'train_name' : row['train_name'],
                        'source' : row['source'],
                        'destination' : row['destination'],
                        'price' : row['price'],
                        'available_seats' : int(row['available_seats']),
                        'seat_numbers' : row['seat_numbers']
                    })
            return "Deleted Successfully !"
    def UpdateRoute(self,train_number,new_source,new_destination,new_price):
        if not os.path.exists('Train.csv'):
            return 'There is no trains Available !'
        with open('Train.csv','r',newline="") as file:
            read = csv.DictReader(file)
            rows = []
            count = 0
            for row in read:
                if row['train_number'] == str(train_number):
                    count += 1
                    row['source'] = new_source
                    row['destination'] = new_destination
                    row['price'] = new_price
                
                rows.append(row)
            if count == 0:
                return "Train doesn't Exists !"
                
            with open('Train.csv','w',newline="") as f1:
                write = csv.DictWriter(f1,fieldnames=fields)
                write.writeheader()
                write.writerows(rows)
            return "Updated successfully !"

    def UpdatePrice(self,train_number,new_price):
            if not os.path.exists('Train.csv'):
                return "There is no trains to update !"
            with open('Train.csv','r') as file:
                read = csv.DictReader(file)
                count = 0
                res = []
                for row in read:
                    if row['train_number'] == str(train_number):
                        row['price'] = new_price
                        count += 1
                    res.append(row)
                if count == 0:
                    return "Train doesn't Exists !"
                with open('Train.csv','w',newline="") as f1:
                    writer = csv.DictWriter(f1,fieldnames=fields)
                    writer.writeheader()
                    writer.writerows(res)
                return "Price updated Successfully"
    def ViewUsers(self):
        if not os.path.exists('User.csv'):
            return "No Users Found !"
        with open('User.csv','r') as file:
            read = csv.DictReader(file)
            print('-'*20,'Users Details','-'*20)
            for row in read:
                print(f"User Name : {row['Name']}")
                print(f"User Email : {row['email']}")
                print(f"User Password : {row['Password']}")
                print('*'*40)
            print('-'*20,'THE END','-'*20)

