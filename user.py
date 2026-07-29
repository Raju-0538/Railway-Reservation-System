import csv
import os
import ast


fields = ['train_number','train_name','source','destination','price','available_seats','seat_numbers']    
field_booked = ['User_email','train_number','Booked_seats','seat_numbers']
class User:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    def register(self,name):
            self.name = name
            if os.path.exists('User.csv'):
                with open('User.csv','r',newline="") as file:
                    read = csv.DictReader(file)
                    for admin in read:
                        if self.email == admin['email']:
                            return "User Already Exists !"
            with open('User.csv','a+',newline="") as file:
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
        with open('User.csv','r',newline="") as file:
            read = csv.DictReader(file)
            for row in read:
                if row['email'] == self.email:
                    if row['Password'] == self.password:
                        return "Login Successfull !"
                    
            return "Invalid Email or password !" 
    def SearchTrain(self,source,destination):
        if not os.path.exists('Train.csv'):
            return "There is No trains available !"
        with open('Train.csv','r') as file:
            read = csv.DictReader(file)
            count = 0
            print('-'*10,"Available Trains are : ",'-'*10)
            for row in read:
                if row['source'] == source and row['destination'] == destination:
                    count += 1
                    print('*'*50)
                    print(f"Train Number : {row['train_number']}")
                    print(f"Source : {row['source']}")
                    print(f"Destination : {row['destination']}")
                    print(f"Ticket Price : {row['price']}")
                    print(f"Available Seats Numbers : {row['seat_numbers']}")
            if count == 0:
                print("There is no trains available in the route")
            print('-'*20,'THE END','-'*20)
    def ViewAvailableSeats(self):
        with open('Train.csv','r') as file:
            read = csv.DictReader(file)
            count = sum(1 for i in read)
            file.seek(78)
            if count >= 0:
                # print(list(read))
                print('-'*10,"Available Trains are : ",'-'*10)
                for row in read:
                    if int(row['available_seats']) > 0:
                        print('*'*50)
                        print(f"Train Number : {row['train_number']}")
                        print(f"Train Name : {row['train_name']}")
                        print(f"Ticket Price : {row['price']}")
                        print(f"No of Available seats : {row['available_seats']}")
                        print(f"Available Seats Numbers : {row['seat_numbers']}")
            else:
                print("No Trains Available for Booking !")
        print('-'*20,'THE END','-'*20)
    def BookTicket(self,train_number,quantity,seat_nos):
        with open('Train.csv','r') as file1:
            read1 = csv.DictReader(file1)
            res2 = []
            f = 0
            for row in read1:
                if str(train_number) == row['train_number']:
                    f += 1
                    available = ast.literal_eval(row['seat_numbers'])
                    if quantity <= int(row['available_seats']) and all(seat in available for seat in seat_nos):
                        if quantity == len(seat_nos):
                            
                            val = int(row['available_seats'])
                            row['available_seats'] = val-quantity
                            avail_seats = ast.literal_eval(row['seat_numbers'])
                            upd_seats = [x for x in avail_seats if int(x) not in seat_nos]
                            row['seat_numbers'] = str(upd_seats)
                            with open('Booked_Tickets.csv','r') as file2:
                                read2 = csv.DictReader(file2)
                                res1 = []
                                found = False
                                for row1 in read2:
                                    if self.email == row1['User_email']:
                                        
                                        if str(train_number) == row1['train_number']:
                                            found = True
                                            row1['Booked_seats'] = str(int(row1['Booked_seats']) + quantity)
                                            updated_seats = ast.literal_eval(row1['seat_numbers'])
                                            updated_seats = sorted(set(updated_seats + seat_nos))
                                            row1['seat_numbers'] = str(updated_seats)
                                        
                                    res1.append(row1)
                                if not found:
                                    res1.append({
                                        'User_email': self.email,
                                        'train_number': train_number,
                                        'Booked_seats': str(quantity),
                                        'seat_numbers': str(seat_nos)
                                    })
                                
                                with open('Booked_Tickets.csv','w',newline="") as file3:
                                    write = csv.DictWriter(file3,fieldnames=field_booked)
                                    write.writeheader()
                                    write.writerows(res1)
                            
                        else:
                            if quantity < len(seat_nos):
                                return f"You have entered {quantity} Tickets and Entered {len(seat_nos)} Seat Numbers !"
                            else:
                                return f"You have entered {quantity} Tickets and Entered {len(seat_nos)} Seat Numbers only!"
                    else:
                        return "Check the Available Seat numbers or Available Seats"
                res2.append(row)
            with open('Train.csv','w',newline="") as file4:
                write1 = csv.DictWriter(file4,fieldnames=fields)
                write1.writeheader()
                write1.writerows(res2)
            if f == 0:
                return "Invalid Train Number !"
        return "Tickets Booked Successfully !"
            

    def CancelTicket(self, train_number, quantity, seat_nos):
        with open('Booked_Tickets.csv', 'r') as file:
            read = csv.DictReader(file)
            booked_data = []
            user_found = False
            train_found = False
            cancel_success = False
            for row in read:
                if row['User_email'] == self.email:
                    user_found = True
                    if row['train_number'] == str(train_number):
                        train_found = True
                        booked_seats = int(row['Booked_seats'])
                        booked_seat_numbers = ast.literal_eval(row['seat_numbers'])
                        if quantity > booked_seats:
                            return "You have entered more tickets than booked."
                        if quantity != len(seat_nos):
                            return (
                                f"You entered {quantity} tickets but "
                                f"{len(seat_nos)} seat numbers."
                            )
                        if not all(seat in booked_seat_numbers for seat in seat_nos):
                            return "Invalid seat numbers."
                        updated_booked_seats = [
                            seat for seat in booked_seat_numbers
                            if seat not in seat_nos
                        ]
                        row['Booked_seats'] = str(booked_seats - quantity)
                        row['seat_numbers'] = str(updated_booked_seats)
                        cancel_success = True
                        if int(row['Booked_seats']) > 0:
                            booked_data.append(row)
                    else:
                        booked_data.append(row)
                else:
                    booked_data.append(row)
        if not user_found:
            return "User has not booked any tickets."

        if not train_found:
            return "Invalid Train Number!"
        with open('Train.csv', 'r') as file:
            read = csv.DictReader(file)
            train_data = []
            found = False
            for row in read:
                if row['train_number'] == str(train_number):
                    found = True
                    available_seats = int(row['available_seats'])
                    row['available_seats'] = str(
                        available_seats + quantity
                    )
                    current_available = ast.literal_eval(row['seat_numbers'])
                    updated_available = sorted(
                        current_available + seat_nos
                    )
                    row['seat_numbers'] = str(updated_available)
                train_data.append(row)
        if not found:
            return "Train Not Found!"

        with open('Booked_Tickets.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_booked)
            writer.writeheader()
            writer.writerows(booked_data)
        with open('Train.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(train_data)
        if cancel_success:
            return "Tickets Cancelled Successfully!"
        return "Cancellation Failed!"
