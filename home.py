import userdatabase
import garden
import profile
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def home_menu_options(name):
    console.clear()
    console.print(Panel(
        f"[turquoise2]Welcome, {name}! Please select from the following options.[/turquoise2]\n\n"
        "[white]1. Create a New Garden[/white]\n"
        "[white]2. View My Gardens[/white]\n"
        "[white]3. View My Calendar[/white]\n"
        "[white]4. View My Profile[/white]\n"
        "[white]5. Log Out[/white]",
        title="[bold cyan]Home Screen[/bold cyan]",
        border_style="cyan"
    ))
    choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5"])
    return int(choice)

def home_screen(user):
    using = True
    while using:
        input_ans = home_menu_options(user[2])
        if input_ans == 1:
            garden.new_garden(user)
        elif input_ans == 2:
            garden.view_gardens(user)
        elif input_ans == 3:
            console.print("[yellow]Coming soon![/yellow]")
        elif input_ans == 4:
            user = profile.view_profile(user)
            
        else:
            console.print(Panel(
                "[spring_green3]Thank you for visiting your Smart Garden Planner. \n[/spring_green3]" 
                "[spring_green3]See you again soon![/spring_green3]",
                title="[bold green]You Are Successfully Logged Out![/bold green]",
                border_style="green"
            ))
                
            using = False
            break
        
    
