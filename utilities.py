def cm_to_inches(cm):
    return round(cm / 2.54, 2)

def inches_to_cm(inches):
    return round(inches * 2.54, 2)

def get_plant_variety():
    plant_variety_int = 0
    while plant_variety_int not in range(1, 5):
        try:
            plant_variety_int = int(input("What kinds of plants would you like in your garden? \n"
                            " 1. Fruits \n 2. Vegetables \n 3. Flowers \n 4. All of the above \n"))
        except ValueError:
            print("Please enter a number between 1-4.")
            plant_variety_int = 0
            
    plant_variety = ""
    if (plant_variety_int == 1):
        plant_variety = "Fruits"
    elif (plant_variety_int == 2):
        plant_variety = "Vegetables"
    elif (plant_variety_int == 3):
        plant_variety = "Flowers"
    else:
        plant_variety = "Mixed"
    return plant_variety

def get_frequency():
    freq_int = 0
    while freq_int not in range(1, 4):
        try:
            freq_int = int(input("What level of maintainence plants do you prefer? \n" 
                        " 1. Low (Watering weekly or less) \n 2. Medium (Watering a few days per week) \n 3. High (Watering daily) \n"))
        except ValueError:
            print("Please enter a number between 1-3.")
            freq_int = 0

    frequency = ""
    if (freq_int == 1): 
        frequency = "Low"
    elif (freq_int == 2):
        frequency = "Medium"
    else: 
        frequency = "High"
    return frequency