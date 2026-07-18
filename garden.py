import gardendatabase
import utilities

def new_garden(user):
    print("Let's create a new garden!")
    unit_label = "cm" if user[5] == "metric" else "inches"
    
    input_garden_type = 0
    while input_garden_type not in range(1, 4):
        try: 
            input_garden_type = int(input("What type of garden is this? Type in the number only! \n 1. Container (Individual)\n 2. In-Ground Garden\n 3. Raised Bed Garden\n"))
        except ValueError:
            print("Not a valid answer. Please only type in the number.") 

    garden_type = ""
    if input_garden_type == 1:
        garden_type = "Container"
    elif input_garden_type == 2:
        garden_type = "In-Ground"
    else:
        garden_type = "Raised Bed"
    
    input_shape = 0
    while input_shape not in range(1, 3):
        try: 
            input_shape = int(input("What shape is the garden? Type in the number only! \n 1. Circular \n 2. Rectangular"))
        except ValueError:
            print("Not a valid answer. Please only type in the number.") 

    shape = ""
    if input_shape == 1:
        shape = "Circular"
        diameter = float(input(f"Enter the diameter of your garden (in {unit_label}): "))
        if unit_label == "cm": 
            diameter = utilities.cm_to_inches(diameter)
        gardendatabase.create_new_garden(user[0], garden_type, shape, None, None, diameter)
    
    elif input_shape == 2:
        shape = "Rectangular"
        length = float(input(f"Enter the length of your garden (in {unit_label}): "))
        width = float(input(f"Enter the width of your garden (in {unit_label}): "))
        if unit_label == "cm":
            length = utilities.cm_to_inches(length)
            width = utilities.cm_to_inches(width)
        gardendatabase.create_new_garden(user[0], garden_type, shape, length, width, None)