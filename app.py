from admin import Admin
from user import User

if __name__ == "__main__":
    print("1.Admin\n2.User")
    try:
        a = int(input("Select a choice 1 or 2 : "))
        if a == 1:
                try :
                    print("1. Register\n2. Login")
                    choice = int(input("Enter a valid choice 1 or 2 : "))
                except Exception as e:
                    print(f"Execution is stopped due to {e}")
                if choice == 1:
                    try:
                        email = input("Email : ")
                        name = input("Name : ")
                        password = input("Password : ")
                        obj = Admin(email,password)
                        print(obj.register(name))
                    except Exception as e:
                        print(f"Execution is stopped due to {e}")
                elif choice == 2:
                    try:
                        email = input("Enter your Email : ")
                        password = input("Enter your password : ")
                        obj = Admin(email,password)
                        choice2 = obj.login()
                        print(choice2)
                    except Exception as e:
                        print(f"Execution is stopped due to {e}")
                    while choice2 == "Login Successfull !":
                        try:
                            print("1.View All Users\n2. View All Booked Tickets\n3. Add Train\n4. Delete Train\n5. Update Route\n6. Update Ticket Price\n7. View Trains Information\n8. Logout")
                            n = int(input("Enter your choice from 1-7: "))
                            if n == 1:
                                obj.ViewUsers()
                            elif n == 2:
                                obj.ViewAllBookedTickets()
                            if n == 3:
                                try:
                                    tnumber = int(input("Enter Train Number : "))
                                    tname = input("Enter Train Name : ").title()
                                    source = input("Enter The Source : ").title()
                                    destination = input("Enter the Destination : ").title()
                                    price = int(input("Enter the price of the Ticket : "))
                                    Aseats = int(input("Enter the No of Tickets Available :  "))
                                    no_of_Tickets = list(map(int,input("Enter the seat numbers seperated by commas : ").split(',')))
                                    print(obj.AddTrain(train_number=tnumber,
                                                        train_name=tname,
                                                        source=source,
                                                        destination=destination,
                                                        price=price,
                                                        available_seats=Aseats,
                                                        seat_numbers=no_of_Tickets))
                                except Exception as e:
                                    print(f"Execution is stopped due to {e}")
                                
                            elif n == 4:
                                try:
                                    tnumber = int(input("Enter Train Number : "))
                                    print(obj.DeleteTrain(tnumber))
                                except Exception as e:
                                    print(e)
                            elif n == 5:
                                try:
                                    tnumber = int(input("Enter the Train Number : "))
                                    new_source = input("Enter the New Source : ").title()
                                    new_destination = input("Enter the New Destination : ").title()
                                    new_price = int(input("Enter the New Ticket Price : "))
                                    print(obj.UpdateRoute(tnumber,new_source,new_destination,new_price))
                                except Exception as e:
                                    print(f"Execution is stopped due to {e}")
                            elif n == 6:
                                try:
                                    tnumber = int(input("Enter Train Number : "))
                                    New_price = int(input("Enter the New Price of Ticket : "))
                                    print(obj.UpdatePrice(tnumber,New_price))
                                except Exception as e:
                                    print(f"Execution is stopped due to {e}")
                            elif n == 7:
                                obj.ViewAvailableSeats()
                            elif n == 8:
                                print("Thank you for your Service !")
                                exit()
                            else:
                                print("Enter valid choice from 1 to 6")
                        except Exception as e:
                            print(f"Execution is stopped due to {e}")
        elif a == 2:
            try:
                print("1. Register\n2. Login")
                choice = int(input("Enter a valid choice 1 or 2 : "))
            
                if choice == 1:
                    try:
                        email = input("Enter your email : ")
                        password = input("Enter your Password : ")
                        name = input("Enter Your Name : ")
                        obj = User(email,password)
                        print(obj.register(name))
                    except Exception as e:
                        print(f"Execution is stopped due to {e}")
                elif choice == 2:
                    try:
                        email = input("Enter your Email : ")
                        password = input("Enter your password : ")
                        obj = User(email,password)
                        choice2 = obj.login()
                        print(choice2)
                    except Exception as e:
                        print(f"Execution is stopped due to {e}")
                    while choice2 == 'Login Successfull !':
                        try:
                            print("1. Search train\n2. View Available Seats\n3. Book Tickets\n4. View Booked Seats\n5. Cancel Tickets\n6. Logout")
                            choice1 = int(input("Enter your choice from 1 to 6 : "))
                        except Exception as e:
                            print(f"Execution is stopped due to {e}")
                        if choice1 == 1:
                            try:
                                source = input("Enter Source : ").title()
                                dest = input("Enter the Destination : ").title()
                                obj.SearchTrain(source,dest)
                            except Exception as e:
                                print(f"Execution is stopped due to {e}")
                        elif choice1 == 2:
                            obj.ViewAvailableSeats()
                        elif choice1 == 3:
                            try:
                                tnumber = int(input("Enter the Train Number : "))
                                print("Before Entering the No of Tickets please Verify the Available Seats !")
                                quantity = int(input("Enter the No of Tickets : "))
                                seat_numbers = list(map(int,input("Enter the Seat Numbers in single line with commas : ").split(',')))
                                print(obj.BookTicket(tnumber,quantity,seat_numbers))
                            except Exception as e:
                                print(f"Execution is stopped due to {e}")
                        elif choice1 == 4:
                            obj.ViewBookedTickets()
                        elif choice1 == 5:
                            try:
                                tnumber = int(input("Enter Train Number : "))
                                print("Before Entering the No of Seats Check your total No of Tickets")
                                quantity = int(input("Enter the No of Tickets : "))
                                print("Before Entering the Seats Numbers Check your Booked Tickets Seat Numbers")
                                seat_numbers = list(map(int,input("Enter the Seat Numbers in single line with commas : ").split(',')))
                                res = obj.CancelTicket(tnumber,quantity,seat_numbers)
                                print(res)
                            except Exception as e:
                                print(f"Execution is stopped due to {e}")
                        elif choice1 == 6:
                            print("Thanks for Visiting !")
                            exit()
                        else:
                            print("Enter valid choice form 1 to 6")
            except Exception as e:
                print(f"Execution is stopped due to {e}")

    except Exception as e:
        print(e)