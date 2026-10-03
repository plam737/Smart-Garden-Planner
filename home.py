import userdatabase
import utilities
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def home_menu_options(name):
    console.clear()
    console.print(Panel(
        f"[turquoise2]Welcome, {name}! Please select from the following options.[/turquoise2]\n\n"
        "[white]1. Create a New Garden\n"
        "2. View My Gardens\n"
        "3. Edit or Delete a Garden\n"
        "4. Add a Plant to a Garden\n"
        "5. View My Profile\n"
        "6. View My Calendar\n"
        "7. SoCal Planting Calendar\n"
        "8. California Native Plant Database\n"
        "9. Log Out[/white]",
        title="[bold cyan]Home Screen[/bold cyan]",
        border_style="cyan"
    ))
    choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9"], default="9")
    return int(choice)

def home_screen(user):
    using = True
    while using:
        input_ans = home_menu_options(user[2])
        if input_ans == 1:
            utilities.console.print("[yellow]Coming soon![/yellow]")
        elif input_ans == 2:
            utilities.console.print("[yellow]Coming soon![/yellow]")
        elif input_ans == 3:
            utilities.console.print("[yellow]Coming soon![/yellow]") 
        elif input_ans == 4:
            utilities.console.print("[yellow]Coming soon![/yellow]")
        elif input_ans == 5:
            utilities.console.print("[yellow]Coming soon![/yellow]")
        elif input_ans == 6:
            utilities.console.print("[yellow]Coming soon![/yellow]")
        elif input_ans == 7:
            utilities.console.print("[yellow]Coming soon![/yellow]")
        elif input_ans == 8:
            utilities.console.print("[yellow]Coming soon![/yellow]")
        else:
            utilities.console.print(Panel(
                "[spring_green3]Thank you for visiting your Smart Garden Planner. \n[/spring_green3]" 
                "[spring_green3]See you again soon![/spring_green3]",
                title="[bold green]You Are Successfully Logged Out![/bold green]",
                border_style="green"
            ))
                
            using = False
            break