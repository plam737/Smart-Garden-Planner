import gardendatabase
import utilities
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt
from rich.prompt import IntPrompt
from rich.table import Table
from rich.prompt import Confirm

console = Console()

def new_garden(user):
    console.clear()
    unit_label = "cm" if user[5] == "metric" else "inches"

    garden_type = utilities.get_garden_type()
    shape, length, width, diameter = utilities.get_shape_and_dimensions(unit_label)
    
    gardendatabase.create_new_garden(user[0], garden_type, shape, length, width, diameter)

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

def edit_delete_garden(user):
    gardens = gardendatabase.get_user_gardens(user[0])
    
    if len(gardens) == 0:
        console.print("[yellow]You have no gardens to edit or delete![/yellow]")
        return

    view_gardens(user)

    console.print(Rule(
        title="Which garden would you like to edit or delete?",
        style="gold3"
    ))
    selected_garden_number = IntPrompt.ask("Select a garden: ", choices=[str(i+1) for i in range(len(gardens))])
    selected_garden = gardens[selected_garden_number - 1]

    console.print(Panel(
        "[light_goldenrod3]Would you like to edit or delete a garden?[/light_goldenrod3]\n"
        "[white]1. Edit a garden \n"
        "2. Delete a garden [/white]",
        title="[gold3]Edit or Delete[/gold3]",
        border_style="gold3"
    ))
    action = Prompt.ask("Select an option: ", choices=["1", "2"])
    if action == "1":
        unit_label = "cm" if user[5] == "metric" else "inches"
        new_garden_type = utilities.get_garden_type(default = selected_garden[2])
        new_shape, new_length, new_width, new_diameter = utilities.get_shape_and_dimensions(unit_label, selected_garden[4], selected_garden[5], selected_garden[6])
        gardendatabase.update_garden(selected_garden[0], user[0], new_garden_type, new_shape, new_length, new_width, new_diameter)
        console.print(("[bold green]Garden updated successfully![/bold green]"))
    elif action == "2":
        if Confirm.ask("Are you sure you want to delete this garden? [y/n]: "):
            gardendatabase.delete_garden(selected_garden[0], user[0])
            console.print(("[bold green]Garden deleted successfully![/bold green]"))
