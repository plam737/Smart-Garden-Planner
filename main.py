import hardiness

def hardiness_zone(city, state):
    lon, lat = hardiness.get_coordinates(city, state)
    if lat is None or lon is None:
        return "NO"
    else: 
        zone = hardiness.get_hardiness_zone(lon, lat, state)
        return zone

def new_user():
    print("Welcome to Smart Garden Planner! \n" 
    "Before we begin, let's ask you a few questions.")
    state = input("Which state or province do you live in? ")
    city = input("What city do you live in? ")
    garden_type = input("What kind of garden do you have? \n" 
    " 1. Container Garden \n 2. In-Ground Garden\n 3. Raised Bed Garden \n 4. Other \n")
    plant_variety = input("What kinds of plants would you like in your garden? \n" \
    " 1. Fruits \n 2. Vegetables \n 3. Flowers \n 4. All of the above \n")
    frequency = input ("What level of maintainence plants do you prefer? \n" 
    " 1. Low \n 2. Medium \n 3. High \n")
    print("Congratulations! You are now a smart gardener!")
    name = input("What is your name? ")
    zone_result = hardiness_zone(city, state)
    print(f"Welcome, {name}!")
    if zone_result == "NO":
        pass
    else: 
        print(f"Because you live in {city}, {state}, your hardiness zone is {zone_result}!")

def user_menu_options():
    choice = int(input("Welcome to the Smart Garden Planner! \n"
    "Please select from the following options. \n"
    "1. Returning User \n"
    "2. New User \n"))
    return choice

def main():
    user_status = user_menu_options()
    if (user_status == 1):
        print("Welcome Back!")
    elif (user_status == 2):
        new_user()

if __name__ == '__main__':
    main()