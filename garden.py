import gardendatabase
import utilities
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def new_garden(user):
    console.clear()
    unit_label = "cm" if user[5] == "metric" else "inches"
    
    console.print(Panel(
        "[magenta]What type of garden is this?[/magenta]\n\n"
        "[white]1. Container (Individual)\n"
        "2. In-Ground Garden\n"
        "3. Raised Bed Garden[/white]",
        title="[bold dark_magenta]Create a New Garden[/bold dark_magenta]",
        border_style="dark_magenta"
    ))
    input_garden_type = int(Prompt.ask("Select an option", choices=["1", "2", "3"]))

    garden_type = {
        1: "Container",
        2: "In-Ground",
        3: "Raised Bed"
    }[input_garden_type]

    console.print(Panel(
        "[magenta]What shape is the garden?[magneta]\n\n"
        "[white]1. Circular\n"
        "2. Rectangular[/white]",
        title="[bold dark_magenta]Garden Shape[/bold dark_magenta]",
        border_style="dark_magenta"
    ))
    input_shape = int(Prompt.ask("Select an option", choices=["1", "2"]))

    if input_shape == 1:
        shape = "Circular"
        console.print(Rule("[magenta]Dimensions[/magenta]", style="magenta"))
        diameter = float(Prompt.ask(f"Enter the diameter of your garden (in {unit_label})"))
        if unit_label == "cm":
            diameter = utilities.cm_to_inches(diameter)
        gardendatabase.create_new_garden(user[0], garden_type, shape, None, None, diameter)

    elif input_shape == 2:
        shape = "Rectangular"
        console.print(Rule("[magenta]Dimensions[/magenta]", style="magenta"))
        length = float(Prompt.ask(f"Enter the length of your garden (in {unit_label})"))
        width = float(Prompt.ask(f"Enter the width of your garden (in {unit_label})"))
        if unit_label == "cm":
            length = utilities.cm_to_inches(length)
            width = utilities.cm_to_inches(width)
        gardendatabase.create_new_garden(user[0], garden_type, shape, length, width, None)

    console.print(f"\n[bold dark_magenta]Garden created successfully![/bold dark_magenta]\n")

def view_gardens(user):
    console.clear()
    gardens = gardendatabase.get_user_gardens(user[0])

    if len(gardens) == 0:
        console.print(Panel(
            "[yellow]You have no gardens yet! Please add a new garden.[/yellow]",
            title="[bold green]My Gardens[/bold green]",
            border_style="green"
        ))
        return

    table = Table(title="My Gardens", border_style="magenta", header_style="bold magenta")
    table.add_column("#", style="white", width=4)
    table.add_column("Type", style="white")
    table.add_column("Shape", style="white")
    table.add_column("Dimensions", style="white")

    for i, garden in enumerate(gardens):
        dimensions = utilities.display_dimensions(garden, user)
        table.add_row(
            str(i + 1),
            garden[2],
            garden[3],
            dimensions
        )

    console.print(table)