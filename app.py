from admin import Admin
from user import User

print("1.Admin\n2.User")
a = int(input("Select a choice 1 or 2 : "))
if a == 1:
        print("1. Register\n2. Login")
        choice = int(input("Enter a valid choice 1 or 2 : "))
        if choice == 1:
            email = input("Email : ")
            name = input("Name : ")
            password = input("Password : ")
            obj = Admin(email,password)
            print(obj.register(name))
        elif choice == 2:
            email = input("Enter your Email : ")
            password = input("Enter your password : ")
            obj = Admin(email,password)
            choice2 = obj.login()
            print(choice2)
            while choice2 == "Login Successfull !":
                print("1. Add Train\n2. Delete Train\n3. Update Route\n4. Update Ticket Price\n5. Logout")
                n = int(input("Enter your choice : "))
                if n == 1:
                    tnumber = int(input("Enter Train Number : "))
                    tname = input("Enter Train Name : ").title()
                    source = input("Enter The Source : ").title()
                    destination = input("Enter the Destination : ").title()
                    price = int(input("Enter the price of the Ticket : "))
                    Aseats = int(input("Enter the Available Seats : "))
                    print(obj.AddTrain(tnumber,tname,source,destination,price,Aseats))
                elif n == 2:
                    tnumber = int(input("Enter Train Number : "))
                    print(obj.DeleteTrain(tnumber))
                elif n == 3:
                    tnumber = int(input("Enter the Train Number : "))
                    new_source = input("Enter the New Source : ").title()
                    new_destination = input("Enter the New Destination : ").title()
                    new_price = int(input("Enter the New Ticket Price : "))
                    print(obj.UpdateRoute(tnumber,new_source,new_destination,new_price))
                elif n == 4:
                    tnumber = int(input("Enter Train Number : "))
                    New_price = int(input("Enter the New Price of Ticket : "))
                    print(obj.UpdatePrice(tnumber,New_price))
                elif n == 5:
                    print("Thank you for your Service !")
                    exit()
                else:
                    print("Enter valid choice from 1 to 6")
elif a == 2:
    print("1. Register\n2. Login")
    choice = int(input("Enter a valid choice 1 or 2 : "))
    if choice == 1:
        email = input("Enter your email : ")
        password = input("Enter your Password : ")
        name = input("Enter Your Name : ")
        obj = User(email,password)
        print(obj.register(name))
    elif choice == 2:
        email = input("Enter your Email : ")
        password = input("Enter your password : ")
        obj = User(email,password)
        choice2 = obj.login()
        print(choice2)
        while choice2 == 'Login Successfull !':
            print("1. Search train\n2. View Available Seats\n3. Book Tickets\n4. Cancel Tickets\n5. Logout")
            choice1 = int(input("Enter your choice from 1 to 6 : "))
            if choice1 == 1:
                source = input("Enter Source : ").title()
                dest = input("Enter the Destination : ").title()
                obj.SearchTrain(source,dest)
            elif choice1 == 2:
                obj.ViewAvailableSeats()
            elif choice1 == 3:
                tnumber = int(input("Enter the Train Number : "))
                print("Before Entering the No of Tickets please Verify the Available Seats !")
                quantity = int(input("Enter the No of Tickets : "))
                seat_numbers = list(map(int,input("Enter the Seat Numbers in single line with commas : ").split(',')))
                print(obj.BookTicket(tnumber,quantity,seat_numbers))
            elif choice1 == 4:
                tnumber = int(input("Enter Train Number : "))
                print("Before Entering the No of Seats Check your total No of Tickets")
                quantity = int(input("Enter the No of Tickets : "))
                print("Before Entering the Seats Numbers Check your Booked Tickets Seat Numbers")
                seat_numbers = list(map(int,input("Enter the Seat Numbers in single line with commas : ").split(',')))
                res = obj.CancelTicket(tnumber,quantity,seat_numbers)
                print(res)
            elif choice1 == 5:
                print("Thanks for Visiting !")
                exit()
            else:
                print("Enter valid choice form 1 to 6")



# name = input("Name : ")
# pas = input("Password : ")
# email = input("Email : ")
# obj = User(email,pas)
# obj.ViewAvailableSeats()
# obj = Admin(email,pas)
# obj.SearchTrain('Vizag','Chennai')
# print(obj.SearchTrain('Vizag','Chennai'))
# print(obj.UpdateRoute(101,'JRG','HYD',2000))
# obj = Admin('raju@gmail.com','Raju@9030')
# print(obj.AddTrain('101','Vandhe Bharath','Vizag','Chennai',2000,15))
# print(obj.AddTrain('102','MEMU Express','Vizag','Kakinada',2000,10))
# print(obj.AddTrain('103','Kachiguada Express','Kachiguda','Nandyala',1000,20))
# print(obj.AddTrain(train_number=104,train_name='Kachiguada Express',source='Vizag',destination='Chennai',price=1000,available_seats = 20))
# print(obj.BookTicket(106,5))

# print(obj.DeleteTrain(101))