from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule

console = Console()

def cm_to_inches(cm):
    return round(cm / 2.54, 2)

def inches_to_cm(inches):
    return round(inches * 2.54, 2)

def get_plant_variety():
    console.print(Panel(
        "[light_goldenrod3]What kinds of plants would you like to grow?[/light_goldenrod3]\n\n"
        "[white]1. Fruits\n"
        "2. Vegetables\n"
        "3. Flowers\n"
        "4. All of the above[/white]",
        title="[bold gold3]Plant Variety[/bold gold3]",
        border_style="gold3"
    ))
    plant_variety_int = Prompt.ask("Select an option", choices=["1", "2", "3", "4"])
    plant_variety = {
        "1": "Fruits",
        "2": "Vegetables",
        "3": "Flowers",
        "4": "Mixed"
    }[plant_variety_int]
    return plant_variety

def get_frequency():
    console.print(Panel(
        "[light_goldenrod3]How often can you water your plants?[/light_goldenrod3]\n\n"
        "[white]1. Low (Watering weekly or less)\n"
        "2. Medium (Watering a few days per week)\n"
        "3. High (Watering daily)[/white]",
        title="[bold gold3]Maintenance Level[/bold gold3]",
        border_style="gold3"
    ))
    freq_int = Prompt.ask("Select an option", choices=["1", "2", "3"])
    frequency = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }[freq_int]
    return frequency

def display_dimensions(garden, user):
    length = garden[4]
    width = garden[5]
    diameter = garden[6]
    if user[5] == "metric":
        unit_label = "cm"
        if garden[3] == "Circular":
            diameter = inches_to_cm(diameter)
        elif garden[3] == "Rectangular":
            length = inches_to_cm(length)
            width = inches_to_cm(width)
    else:
        unit_label = "inches"
    if garden[3] == "Circular":
        dimension_string = f"Diameter: {diameter} {unit_label}"
    elif garden[3] == "Rectangular":
        dimension_string = f"{length} x {width} {unit_label}"
    return dimension_string

def get_garden_type(default=None):
    console.print(Panel(
            "[magenta]What type of garden is this?[/magenta]\n\n"
            "[white]1. Container (Individual)\n"
            "2. In-Ground Garden\n"
            "3. Raised Bed Garden[/white]",
            title="[bold dark_magenta]Garden Type[/bold dark_magenta]",
            border_style="dark_magenta"
        ))
    
    input_garden_type = int(Prompt.ask("Select an option", choices=["1", "2", "3"], default=default))

    garden_type = {
        1: "Container",
        2: "In-Ground",
        3: "Raised Bed"
    }[input_garden_type]

    return garden_type

def get_shape_and_dimensions(unit_label, def_length = None, def_width = None, def_diameter = None):
    shape = ""
    length = def_length
    width = def_width
    diameter = def_diameter
    console.print(Panel(
        "[magenta]What shape is the garden?[/magenta]\n\n"
        "[white]1. Circular\n"
        "2. Rectangular[/white]",
        title="[bold dark_magenta]Garden Shape[/bold dark_magenta]",
        border_style="dark_magenta"
    ))

    input_shape = int(Prompt.ask("Select an option", choices=["1", "2"]))
    
    if input_shape == 1:
        shape = "Circular"
        console.print(Rule("[magenta]Dimensions[/magenta]", style="magenta"))
        diameter = float(Prompt.ask(
            f"Enter the diameter of your garden (in {unit_label})",
            default=str(def_diameter) if def_diameter else None
        ))
        if unit_label == "cm":
            diameter = cm_to_inches(diameter)

    elif input_shape == 2:
        shape = "Rectangular"
        console.print(Rule("[magenta]Dimensions[/magenta]", style="magenta"))
        length = float(Prompt.ask(f"Enter the length", default=str(def_length) if def_length else None))
        width = float(Prompt.ask(f"Enter the width", default=str(def_width) if def_width else None))
        if unit_label == "cm":
            length = cm_to_inches(length)
            width = cm_to_inches(width)

    return shape, length, width, diameter