import hardiness
import userdatabase
import getpass

def hardiness_zone(city, state):
    lon, lat = hardiness.get_coordinates(city, state)
    if lat is None or lon is None:
        return "NO"
    else: 
        zone = hardiness.get_hardiness_zone(lon, lat, state)
        return zone

def new_user_initiation():
    print("Welcome to Smart Garden Planner! \n" 
    "Before we begin, let's ask you a few questions.")
    
    state = input("Which state or province do you live in? ")
    city = input("What city do you live in? ")
    
    garden_type = 0
    while garden_type not in range(1, 5):
        try:
            garden_type = int(input("What kind of garden do you have? \n" 
                            " 1. Container Garden \n 2. In-Ground Garden\n 3. Raised Bed Garden \n 4. Mixed (a mix of Container, In-Ground, and Raised Bed) \n"))
        except ValueError:
            print("Please enter a number between 1-4.")
            garden_type = 0  

    plant_variety = 0
    while plant_variety not in range(1, 5):
        try:
            plant_variety = int(input("What kinds of plants would you like in your garden? \n"
                            " 1. Fruits \n 2. Vegetables \n 3. Flowers \n 4. All of the above \n"))
        except ValueError:
            print("Please enter a number between 1-4.")
            plant_variety = 0

    frequency = 0
    while frequency not in range(1, 4):
        try:
            frequency = int(input("What level of maintainence plants do you prefer? \n" 
                        " 1. Low (Watering weekly or less) \n 2. Medium (Watering a few days per week) \n 3. High (Watering daily) \n"))
        except ValueError:
            print("Please enter a number between 1-3.")
            frequency = 0
                
    print("Congratulations! You are now a smart gardener!")
    
    name = input("What is your name? ")
    username = input("What username would you like? ")
    password = getpass.getpass("What password would you like?")
    hard_zone = hardiness_zone(city, state)
    
    new_user_creation(username, password, name, city, state, garden_type, plant_variety, frequency, hard_zone)

    print(f"Welcome, {name}!")
    if hard_zone == "NO":
        pass
    else: 
        print(f"Because you live in {city}, {state}, your hardiness zone is {hard_zone}!")

def new_user_creation(username, password, name, city, state, garden_type, plant_variety, frequency, hard_zone):
    
    if (garden_type == 1):
        garden_type = "Container"
    elif (garden_type == 2):
        garden_type = "In-Ground"
    elif (garden_type == 3):
        garden_type = "Raised Bed"
    else:
        garden_type = "Mixed"

    if (plant_variety == 1):
        plant_variety = "Fruits"
    elif (plant_variety == 2):
        plant_variety = "Vegetables"
    elif (plant_variety == 3):
        plant_variety = "Flowers"
    else:
        plant_variety = "Mixed"
    
    if (frequency == 1): 
        frequency = "Low"
    elif (frequency == 2):
        frequency = "Medium"
    else: 
        frequency = "High"

    userdatabase.create_new_user(username, password, name, city, state, garden_type, plant_variety, frequency, hard_zone)