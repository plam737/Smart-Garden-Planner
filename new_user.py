import hardiness
import userdatabase
import utilities
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt

def new_user_initiation():
    utilities.console.clear()
    utilities.console.print(Panel( "[orange3]Before we begin, please answer a few questions.[/orange3]",
        title="[bold orange3]Let's Get You Started![/bold orange3]",
        border_style="orange3"
    ))

    utilities.console.print(Rule("[gold3]Location[/gold3]", style="gold3"))
    city = Prompt.ask("What city do you live in?")
    hard_zone = hardiness.hardiness_zone(city)
    while hard_zone == "NO":
        utilities.console.print("[red]Sorry, we could not find your hardiness zone. Please try again.[/red]")
        city = Prompt.ask("What city do you live in?")
        hard_zone = hardiness.hardiness_zone(city)
    units = "imperial"

    utilities.console.print(Rule("[gold3]Personal Information[/gold3]", style="gold3"))
    name = Prompt.ask("What is your name?")
    username = Prompt.ask("What username would you like?")
    while userdatabase.get_user_by_username(username) != "User not found":
        utilities.console.print("[red]Sorry, that username is already taken. Please try again.[/red]")
        username = Prompt.ask("What username would you like?")
    password = Prompt.ask("What password would you like?", password=True)

    userdatabase.create_new_user(username, password, name, city, hard_zone, units)
    return username, password