import argparse
import logging
from rich.console import Console
from rich import print
from rich import pretty

from generate import *

console = Console()
FORMAT = '%(levelname)s %(asctime)s %(filename)s %(lineno)d %(message)s'
logging.basicConfig(
    filename='pypc.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT, datefmt="[%X]",
)

# Basic logging test
# logging.info("Does this work?")

def banner():
    print(r'''
______     ______  _____   +----------------------+
| ___ \    | ___ \/  __ \  | Created by <art3m1s> |
| |_/ /   _| |_/ /| /  \/  +----------------------+
|  __/ | | |  __/ | |      |   Version: 0.1#dev   |
| |  | |_| | |    | \__/\  +----------------------+
\_|   \__, \_|     \____/
       __/ |
      |___/ ''')

def info():
    print('''\n◇ Info:
Python Package Creator (PyPC) is a simple tool to easily generate
standardized project files. It includes several basic configurations,
that can be setup with a click, or you can set up custom configurations.''')

def menu():
    while 1:
        banner()
        print("\n[bold white][[/bold white][green bold]1[/green bold][bold white]][/bold white] [cyan]Generate a new project[/cyan]")
        print("[bold white][[/bold white][green bold]2[/green bold][bold white]][/bold white] [cyan]Create a custom template[/cyan]")
        print("\n[bold white][[/bold white][green bold]3[/green bold][bold white]][/bold white] [cyan]Info[/cyan]")
        print("[bold white][[/bold white][green bold]4[/green bold][bold white]][/bold white] [cyan]LICENSE[/cyan]")
        print("[bold white][[/bold white][green bold]5[/green bold][bold white]][/bold white] [cyan]Exit[/cyan]")


        while 1:
            try:
                ID = int(console.input("\n[bold white][[/bold white][bold yellow]+[/bold yellow][bold white]][/bold white] [cyan]Enter mode ID: [/cyan]"))
                break
            except ValueError:
                print("[bold white][[/bold white][red bold]![/red bold][bold white]][/bold white] [green]Invalid ID (input must be an integer)[/green]")

        if ID == 1:
            generate()
            break
        elif ID == 2:
            create()
            break
        elif ID == 3:
            info()
            break
        elif ID == 4:
            license()
            break
        elif ID == 5:
            quit()
        else:
            print("[bold white][[/bold white][red bold]![/red bold][bold white]][/bold white] [green]Invalid ID (input must be an integer)[/green]")



def main():
    menu()

if __name__ == '__main__':
    main()
