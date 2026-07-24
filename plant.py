import json
import plantdatabase
from datetime import date, datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt, Confirm

console = Console()

def load_plant_list():
    with open("plant_list.json", "r") as f:
        return json.load(f)

plant_list = load_plant_list()

def get_allowed_categories(garden_category):
    mapping = {
        "Fruits": ["Fruit", "Tree"],
        "Vegetables": ["Vegetable", "Herb"],
        "Flowers": ["Flower", "Shrub"],
        "Mixed": []
    }
    return mapping[garden_category]

def search_plants(query, garden_type, garden_category):
    results = plant_list

    if garden_type == "Container":
        results = [p for p in results if p["container_friendly"]]
        console.print("[yellow]Showing only container-friendly plants![/yellow]")

    allowed_categories = get_allowed_categories(garden_category)
    if allowed_categories:
        results = [p for p in results if p["category"] in allowed_categories]
        console.print(f"[yellow]Showing only {garden_category} plants![/yellow]")

    results = [p for p in results if query.lower() in p["plant_name"].lower()]

    return results

def add_plant_to_garden(user, garden_id, garden_type, garden_category):
    searching = True
    while searching:
        console.print(Rule(
                title="[cyan]Let's add a new plant![/cyan]",
                style="cyan"
            ))
        query = Prompt.ask("Search for a plant: ")
        
        res = search_plants(query, garden_type, garden_category)
        if len(res) == 0:
            console.print("[red]Plant not found. Please try again or return to menu.[/red]")
            if Confirm.ask("Would you like to search again?"):
                continue
            else:
                return 
        else:
            searching = False
    table = Table(title="Plants Found", border_style="green", header_style="bold green")
    table.add_column("#", width=4)
    table.add_column("Plant Name", style="spring_green3")
    table.add_column("Type", style="white")
    table.add_column("Spacing (in)", style="white")
    table.add_column("Water (in/wk)", style="white")
    table.add_column("Sun", style="white")
    table.add_column("Container Friendly", style="white")

    for i, plant in enumerate(res):
        table.add_row(
            str(i + 1),
            plant["plant_name"],
            plant["plant_type"],
            str(plant["spacing_inches"]),
            str(plant["water_inches_week"]),
            plant["sun_needs"],
            str(plant["container_friendly"])
        )
    console.print(table)
    selected_plant = Prompt.ask("Selected a plant ", choices=[str(i+1) for i in range(len(res))])
    selected_plant = res[int(selected_plant) - 1]
    planting_date = Prompt.ask("Planting date (DD/MM/YYYY)", default=date.today().strftime("%d/%m/%Y"))
    notes = Prompt.ask("Any notes?", default="")
    plantdatabase.add_plant(garden_id, user[0], selected_plant["plant_name"], planting_date, notes)
    console.print(f"[bold green]✅ {selected_plant['plant_name']} added successfully![/bold green]")

            