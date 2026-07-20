import userdatabase
import hardiness
import utilities

def view_profile(user):
    print(f"Your Profile: \n"
          "-----------------------------------------------\n"
          f"Username: {user[0]}\n"
          f"Name: {user[2]}\n"
          f"City: {user[3]}\n"
          f"State: {user[4]}\n"
          f"Hardiness Zone: {user[8]}\n"
          f"Preferred Plant Variety: {user[6]}\n"
          f"Maintainaince Level: {user[7]}\n"
          f"Units: {user[5].capitalize()}\n"
          "-----------------------------------------------\n"
    )
    update = input("Would you like you update your profile? (y/n) \n"
                   "To return to the home screen, type 'n'. ")
    if update.lower() == "y":
        user = update_profile(user)
        return user
    else: 
        return user
    

def update_profile(user):
    updating = True
    while updating:
        choice = update_profile_menu_options()

        if choice == 1:
            new_name = input("What is your new name?")
            userdatabase.update_name(user[0], new_name)
            user = userdatabase.get_user_by_username(user[0])
        
        elif choice == 2:
            new_city = input("Where is your new city?")
            new_state = input("Where is your new state?")
            new_hard_zone = hardiness.hardiness_zone(new_city, new_state)
            new_units = "metric" if hardiness.is_canada(new_state) else "imperial" 
            userdatabase.update_location(user[0], new_city, new_state, new_hard_zone, new_units)
            user = userdatabase.get_user_by_username(user[0])
        
        elif choice == 3:
            new_uns = ""
            if user[5] == "metric":
                new_uns = "imperial"
            else: 
                new_uns = "metric"
            answer = input(f"Switching units from {user[5]} to {new_uns}. Is that correct? (y/n)")
            if answer.lower() == "y":
                userdatabase.update_units(user[0], new_uns)
                user = userdatabase.get_user_by_username(user[0])
        
        elif choice == 4:
            new_plant_variety = utilities.get_plant_variety()
            userdatabase.update_plant_variety(user[0], new_plant_variety)
            user = userdatabase.get_user_by_username(user[0])

        elif choice == 5:
            new_frequency = utilities.get_frequency()
            userdatabase.update_frequency(user[0], new_frequency)
            user = userdatabase.get_user_by_username(user[0])

        elif choice == 6: 
            updating = False
    return user

def update_profile_menu_options():
    choice = 0
    try:
        choice = int(input(
            f"What would you like to update?\n"
            "-----------------------------------------------\n"
            f"1. Name\n"
            f"2. Location\n"
            f"3. Units\n"
            f"4. Plant Variety\n"
            f"5. Maintainence Level\n"
            f"6. Back\n"      
        ))
        if choice not in range(1,7):
            print("Please enter a number from 1-6.")
    except ValueError:
        print("Please enter a number from 1-6.")
        choice = 0
    return choice
