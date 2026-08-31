import csv
import os


fields = ['train_number','train_name','source','destination','price','available_seats','seat_numbers']
class Admin:
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
    def AddTrain(self,train_number,train_name,source,destination,price,available_seats,seat_numbers):
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

