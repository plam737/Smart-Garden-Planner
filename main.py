import getpass
import userdatabase
import new_user

def user_menu_options():
    choice = int(input("Welcome to the Smart Garden Planner! \n"
    "Please select from the following options. \n"
    "1. Returning User \n"
    "2. New User \n"))
    return choice

def main():
    userdatabase.initialize_db()
    user_status = user_menu_options()
    
    if (user_status == 1):
        user = None
        while user is None or user == "Password incorrect" or user == "User not found":
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            user = userdatabase.find_returning_user(username, password)
            if user == "User not found":
                print("User not found. Please try again.")
            elif user == "Password incorrect":
                print("Password incorrect. Please try again.")
        print(f"Welcome back, {user[2]}!")
    
    elif (user_status == 2):
        new_user.new_user_initiation()

if __name__ == '__main__':
    main()