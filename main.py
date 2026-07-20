import userdatabase
import new_user
import home
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt
from rich.prompt import IntPrompt
from rich.prompt import Confirm

console = Console()

def user_menu_options():
    choice = 0
    while choice not in range(1, 4):
        console.clear()
        console.print(Panel(
            "[spring_green3]Please select from the following options.[/spring_green3]\n\n"
            "[white]1. Returning User\n"
            "2. New User\n"
            "3. Exit[/white]",
            title="[bold green]Welcome to the Smart Garden Planner[/bold green]",
            border_style="green"
        ))
        choice = IntPrompt.ask("Select an option")
    return choice

def main():
    userdatabase.initialize_db()
    using = True
    while using:                                   
        user_status = user_menu_options()
        
        if user_status == 1:
            user = None
            while user is None or user == "Password incorrect" or user == "User not found":
                console.print(Rule(title="[orange3]Login[/orange3]", style="orange3"))
                username = Prompt.ask("Username")
                password = Prompt.ask("Password", password=True) 
                user = userdatabase.find_returning_user(username, password)
                if user == "User not found":
                    console.print("[red]User not found. Please try again.[/red]")
                    if not Confirm.ask("Do you have an account?"):
                        console.print("[yellow]Redirecting to main menu...[/yellow]")
                        break                    
                elif user == "Password incorrect":
                    console.print("[red]Password incorrect. Please try again.[/red]")
            if user and user not in ["User not found", "Password incorrect"]:
                home.home_screen(user)
        
        elif user_status == 2:
            username, password = new_user.new_user_initiation()
            user = userdatabase.find_returning_user(username, password)
            home.home_screen(user)

        elif user_status == 3:
            using = False

if __name__ == '__main__':
    main()