from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

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