import hardiness
import userdatabase
import utilities
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt, IntPrompt

console = Console()

def new_user_initiation():
    console.clear()
    console.print(Panel(
        "[orange3]Before we begin, please answer a few questions.[/orange3]",
        title="[bold orange3]Let's Get You Started![/bold orange3]",
        border_style="orange3"
    ))

    console.print(Rule("[gold3]Location[/gold3]", style="gold3"))
    state = Prompt.ask("Which state or province do you live in?")
    city = Prompt.ask("What city do you live in?")

    units = "metric" if hardiness.is_canada(state) else "imperial"

    console.print(Rule("[gold3]Personal Information[/gold3]", style="gold3"))
    name = Prompt.ask("What is your name?")
    username = Prompt.ask("What username would you like?")
    password = Prompt.ask("What password would you like?", password=True)

    console.print(Rule("[gold3]Garden Preferences[/gold3]", style="gold3"))
    plant_variety = utilities.get_plant_variety()
    frequency = utilities.get_frequency()

    hard_zone = hardiness.hardiness_zone(city, state)
    userdatabase.create_new_user(username, password, name, city, state, units, plant_variety, frequency, hard_zone)
    return username, password