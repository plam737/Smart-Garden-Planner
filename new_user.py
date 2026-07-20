import hardiness
import userdatabase
import getpass
import utilities

def new_user_initiation():
    print("Welcome to Smart Garden Planner! \n" 
    "Before we begin, let's ask you a few questions.")
    
    state = input("Which state or province do you live in? ")
    city = input("What city do you live in? ")

    units = ""
    if hardiness.is_canada(state):
        units = "metric"
    else:
        units = "imperial"

    print("Congratulations! You are now a smart gardener!")
    
    name = input("What is your name? ")
    username = input("What username would you like? ")
    password = getpass.getpass("What password would you like?")
    hard_zone = hardiness.hardiness_zone(city, state)
    plant_variety = utilities.get_plant_variety()
    frequency = utilities.get_frequency()

    userdatabase.create_new_user(username, password, name, city, state, units, plant_variety, frequency, hard_zone)

    print(f"Welcome, {name}!")
    if hard_zone == "NO":
        pass
    else: 
        print(f"Because you live in {city}, {state}, your hardiness zone is {hard_zone}!")
    
    return username, password