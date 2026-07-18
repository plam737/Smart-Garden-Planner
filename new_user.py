import hardiness
import userdatabase
import getpass
import home

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

    units = ""
    if hardiness.is_canada(state):
        units = "metric"
    else:
        units = "imperial"

    print("Congratulations! You are now a smart gardener!")
    
    name = input("What is your name? ")
    username = input("What username would you like? ")
    password = getpass.getpass("What password would you like?")
    hard_zone = hardiness_zone(city, state)
    

    new_user_creation(username, password, name, city, state, units, plant_variety, frequency, hard_zone)

    print(f"Welcome, {name}!")
    if hard_zone == "NO":
        pass
    else: 
        print(f"Because you live in {city}, {state}, your hardiness zone is {hard_zone}!")
    
    return username, password

def new_user_creation(username, password, name, city, state, units, plant_variety, frequency, hard_zone):

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

    userdatabase.create_new_user(username, password, name, city, state, units, plant_variety, frequency, hard_zone)