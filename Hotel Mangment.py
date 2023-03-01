print("    Wellcome To raghava Hotel") 
print("_____________________________________") 
room_prices_list = {'single bed room': '1000', 'double bed room': '2000'} 
room = input("Which room do you want:") 
Bill = 0 
for i in room_prices_list.keys():
    if room == i:
        name = input("Respected sir or mam tell me  your name:")
        phone_no = int(input("enter phone number:"))
        address = input("enter your address:") 

        aviable ='''
        1. breakfast = 500 
        2. lunch = 600 
        3. dinner = 500
        4. wifi = 100
        5. water = 50

        ''' 
    
        print(aviable) 
        print("Dear {}".formate(name),"please select any option:")
        option = int(input("enter your option:"))
        while option < 5:
            if option == 1:
                Bill == Bill+500 
            elif option == 2:
                Bill == Bill+600 
            elif option == 3:
                Bill == Bill+500
            elif option == 4:
                Bill == Bill+100
            elif option == 5:
                Bill == Bill+50
                break 
            else:
                print("Invalid") 
            option = int(input("enter your option:")) 
        Bill = Bill+room_prices_list.get(room) 
    else:
        print("Invalid room") 
    print("    Welcome To raghava's Hotel") 
    print("_____________________________________") 
    print("your name:",name) 
    print("phone_no:",phone_no)
    print("address",address)
    print("Total Bill:",Bill) 
    print("Thank you have nice day visit again") 
    print("______________________________________")


raghavendra
