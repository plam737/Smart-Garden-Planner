import userdatabase
import hardiness
import utilities
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt, Confirm

console = Console()

def view_profile(user):
    console.clear()
    
    console.print(Panel(
        f"[orange3]Username:[/orange3] {user[0]}\n"
        f"[orange3]Name:[/orange3] {user[2]}\n" 
        f"[orange3]City:[/orange3] {user[3]}\n"
        f"[orange3]State:[/orange3] {user[4]}\n"
        f"[orange3]Hardiness Zone:[/orange3] {user[8]}\n"
        f"[orange3]Preferred Plant Variety:[/orange3] {user[6]}\n"
        f"[orange3]Maintenance Level:[/orange3] {user[7]}\n"
        f"[orange3]Units:[/orange3] {user[5].capitalize()}",
        title="[bold dark_orange3]Your Profile[/bold dark_orange3]", 
        border_style="dark_orange3")
    )
    if Confirm.ask("Would you like to update your profile?"):
        user = update_profile(user)
    return user

def update_profile(user):
    updating = True
    while updating:
        choice = update_profile_menu_options()

        if choice == "1":
            new_name = Prompt.ask("What is your new name?")
            userdatabase.update_name(user[0], new_name)
            user = userdatabase.get_user_by_username(user[0])
            console.print("[bold green]Name updated successfully![/bold green]")
        
        elif choice == "2":
            console.print(Rule("[gold3]Update Location[/gold3]", style="gold3"))
            new_city = Prompt.ask("What is your new city?")
            new_state = Prompt.ask("What is your new state or province?")
            new_hard_zone = hardiness.hardiness_zone(new_city, new_state)
            new_units = "metric" if hardiness.is_canada(new_state) else "imperial"
            userdatabase.update_location(user[0], new_city, new_state, new_hard_zone, new_units)
            user = userdatabase.get_user_by_username(user[0])
            console.print("[bold green]Location updated successfully![/bold green]")
        
        elif choice == "3":
            new_uns = "imperial" if user[5] == "metric" else "metric"
            if Confirm.ask(f"Switch units from [bold]{user[5]}[/bold] to [bold]{new_uns}[/bold]?"):
                userdatabase.update_units(user[0], new_uns)
                user = userdatabase.get_user_by_username(user[0])
                console.print("[bold green]Units updated successfully![/bold green]")
        
        elif choice == "4":
            new_plant_variety = utilities.get_plant_variety()
            userdatabase.update_plant_variety(user[0], new_plant_variety)
            user = userdatabase.get_user_by_username(user[0])
            console.print("[bold green]Plant variety updated successfully![/bold green]")

        elif choice == "5":
            new_frequency = utilities.get_frequency()
            userdatabase.update_frequency(user[0], new_frequency)
            user = userdatabase.get_user_by_username(user[0])
            console.print("[bold green]Maintenance level updated successfully![/bold green]")

        elif choice == "6":
            updating = False
    return user

def update_profile_menu_options():
    console.print(Panel(
        "[light_goldenrod3]What would you like to update?[/light_goldenrod3]\n\n"
        "[white]1. Name\n"
        "2. Location\n"
        "3. Units\n"
        "4. Plant Variety\n"
        "5. Maintenance Level\n"
        "6. Back[/white]",
        title="[bold gold3]Update Profile[/bold gold3]",
        border_style="gold3"
    ))
    choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6"])
    return choice