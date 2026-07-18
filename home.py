import userdatabase
import garden

def home_menu_options():
    choice = 0
    try:
        choice = int(input(
            "Please select from the following options. \n"
            "1. Create a New Garden \n"
            "2. View My Gardens \n"
            "3. View My Calendar \n"
            "4. View My Profile \n"
            "5. Log Out \n"
        ))
        if choice not in range(1,6):
            print("Please enter a number from 1-5.")
    except ValueError:
        print("Please enter a number from 1-5.")
        choice = 0
    return choice

def home_screen(user):
    using = True
    print(f"Welcome to your Smart Garden Planner, {user[2]}!")
    while using:
        input_ans = home_menu_options()
        if input_ans == 1:
            garden.new_garden(user)
        elif input_ans == 2:
            print("Coming soon!")
        elif input_ans == 3:
            print("Coming soon!")
        elif input_ans == 4:
            print("Coming soon!")
        else:
            print("You are successfully logged out!\n " \
                "Thank you for visiting your Smart Garden Planner. \n See you again!")
            using = False
        
    
