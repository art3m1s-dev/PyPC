from pypc import *
import os
from rich.tree import Tree
import sys
import shutil
from datetime import datetime
import traceback

console = Console()


def generate():
    try:

        print("[cyan bold]Select one of the following templates to continue\nor inspect a template by calling `inspect <template>`.\nTemplates are called with the name in `<>`.\n To see more commands, enter `help` or `quit` to exit.[/]")
        tree = Tree("\n[white bold]Standard Templates", guide_style="bold")
        tree_g = tree.add("[cyan bold]<CLI> [/][magenta bold]Python CLI Tool (with 'setuptools')")
        tree.add("[cyan bold]<FLASK> [/][magenta bold]Python Web App (with 'Flask')")
        print(tree)

        tree = Tree("\n[white bold]Custom Templates", guide_style="bold")
        tree_c = tree.add("[cyan bold]<std> [/][magenta bold]Python Custom Tool Example")
        tree.add("[cyan bold]<std> [/][magenta bold]Python Custom Template Example 2")
        print(tree)

        while 1:
            cmd = console.input("\n[bold white]pypc ~/# ")
            if cmd.upper() == "CLI":
                print("\n[bold cyan]Please enter a name for your project.")
                name = console.input("[bold white]pypc ~/CLI/RootFolderName: ")

                while 1:
                    try:
                        if os.path.isdir(os.path.expanduser('~') + f"/{name}"):
                            print("[bold red]Folder already exists! Please use a diffent name.")
                            name = console.input("[bold white]pypc ~/CLI/RootFolderName: ")

                        else:
                            os.makedirs(os.path.expanduser('~') + f"/{name}/app")
                            path = os.path.expanduser('~') + "/" + name
                            shutil.copy("templates/CLI/app/__init__.py", f"{path}/app/__init__.py")
                            shutil.copy("templates/CLI/app/__main__.py", f"{path}/app/__main__.py")
                            shutil.copy("templates/CLI/app/application.py", f"{path}/app/application.py")

                            print("\n[bold cyan]Enter a license to use, type `MIT` to use the MIT license, or type `GNU` to use the GNU GPL v3.0.\nTo use a custom license, input `CUSTOM`. This will generate an empty 'LICENSE.txt' file")
                            while 1:
                                license = console.input("[bold white]pypc ~/FLASK/LicenseName: ")

                                if license.upper() == "MIT":
                                    shutil.copy("templates/licenses/MIT_LICENSE", f"{path}/LICENSE")
                                    shutil.copy("templates/CLI/MANIFEST.in", f"{path}/MANIFEST.in")
                                    break

                                elif license.upper() == "GNU":
                                    shutil.copy("templates/licenses/GNU-GPL-v3_LICENSE", f"{path}/LICENSE")
                                    shutil.copy("templates/CLI/MANIFEST.in", f"{path}/MANIFEST.in")
                                    break

                                elif license.upper() == "CUSTOM":
                                    shutil.copy("templates/CLI/MANIFEST.in", f"{path}/MANIFEST.in")
                                    open(f"{path}/LICENSE", 'a').close()
                                    break

                                else:
                                    print("[bold red]Unrecognized license! Please use `MIT`, `GNU` or `CUSTOM`.")

                            open(f"{path}/requirements.txt", 'a').close()
                            open(f"{path}/README.md", 'a').close()
                            open(f"{path}/.gitignore", 'a').close()

                            shutil.copy("templates/CLI/main.py", f"{path}/main.py")
                            shutil.copy("templates/CLI/setup.py", f"{path}/setup.py")

                            print(f"[bold white]Project created at [/bold white][bold cyan]'{path}'")
                            break

                    except KeyboardInterrupt:
                        shutil.rmtree(f"{path}")
                        sys.exit(console.print(f"\n\n[bold red]WARNING: [/bold red][bold white]User Terminated Program Before Setup Was Complete: Project '{name}' Has been Deleted"))




    ###########################################################################################################################


            elif cmd.upper() == "FLASK":
                print("\n[bold cyan]Please enter a name for your project.")
                name = console.input("[bold white]pypc ~/FLASK/RootFolderName: ")

                while 1:
                    try:
                        if os.path.isdir(os.path.expanduser('~') + f"/{name}"):
                            print("[bold red]Folder already exists! Please use a diffent name.")
                            name = console.input("[bold white]pypc ~/FLASK/RootFolderName: ")

                        else:

                            # Create the file tree
                            os.makedirs(os.path.expanduser('~') + f"/{name}/{name}/templates/auth")
                            os.mkdir(os.path.expanduser('~') + f"/{name}/{name}/templates/blog")
                            os.mkdir(os.path.expanduser('~') + f"/{name}/{name}/static")
                            os.mkdir(os.path.expanduser('~') + f"/{name}/tests")



                            path = os.path.expanduser('~') + "/" + name

                            # Create all the files
                            shutil.copy("templates/FLASK/auth.py", f"{path}/{name}/auth.py")
                            shutil.copy("templates/FLASK/db.py", f"{path}/{name}/db.py")
                            shutil.copy("templates/FLASK/schema.sql", f"{path}/{name}/schema.sql")
                            shutil.copy("templates/FLASK/blog.py", f"{path}/{name}/blog.py")

                            shutil.copy("templates/FLASK/index.html", f"{path}/{name}/templates/base.html")
                            shutil.copy("templates/FLASK/index.html", f"{path}/{name}/templates/auth/login.html")
                            shutil.copy("templates/FLASK/index.html", f"{path}/{name}/templates/auth/register.html")

                            shutil.copy("templates/FLASK/index.html", f"{path}/{name}/templates/blog/create.html")
                            shutil.copy("templates/FLASK/index.html", f"{path}/{name}/templates/blog/index.html")
                            shutil.copy("templates/FLASK/index.html", f"{path}/{name}/templates/blog/update.html")

                            shutil.copy("templates/FLASK/style.css", f"{path}/{name}/static/style.css")

                            shutil.copy("templates/FLASK/tests/conftest.py", f"{path}/tests/conftest.py")
                            shutil.copy("templates/FLASK/tests/data.sql", f"{path}/tests/data.sql")
                            shutil.copy("templates/FLASK/tests/test_factory.py", f"{path}/tests/test_factory.py")
                            shutil.copy("templates/FLASK/tests/test_db.py", f"{path}/tests/test_db.py")
                            shutil.copy("templates/FLASK/tests/test_auth.py", f"{path}/tests/test_auth.py")
                            shutil.copy("templates/FLASK/tests/test_blog.py", f"{path}/tests/test_blog.py")

                            shutil.copy("templates/FLASK/setup.py", f"{path}/setup.py")

                            open(f"{path}/.gitignore", 'a').close()
                            open(f"{path}/{name}/__init__.py", 'a').close()

                            print("\n[bold cyan]Enter a license to use, type `MIT` to use the MIT license, or type `GNU` to use the GNU GPL v3.0.\nTo use a custom license, input `CUSTOM`. This will generate an empty 'LICENSE.txt' file")
                            while 1:
                                license = console.input("[bold white]pypc ~/FLASK/LicenseName: ")

                                if license.upper() == "MIT":
                                    shutil.copy("templates/FLASK/MANIFEST.in", f"{path}/MANIFEST.in")
                                    shutil.copy("templates/licenses/MIT_LICENSE", f"{path}/LICENSE")
                                    break

                                elif license.upper() == "GNU":
                                    shutil.copy("templates/FLASK/MANIFEST.in", f"{path}/MANIFEST.in")
                                    shutil.copy("templates/licenses/GNU-GPL-v3_LICENSE", f"{path}/LICENSE")
                                    break

                                elif license.upper() == "CUSTOM":
                                    shutil.copy("templates/FLASK/MANIFEST.in", f"{path}/MANIFEST.in")
                                    open(f"{path}/LICENSE", 'a').close()
                                    break

                                else:
                                    print("[bold red]Unrecognized license! Please use `MIT`, `GNU` or `CUSTOM`.")

                            print(f"[bold white]Project created at [/bold white][bold cyan]'{path}'")
                            test.test()
                            break

                    except KeyboardInterrupt:
                        shutil.rmtree(f"{path}")
                        sys.exit(console.print(f"\n\n[bold red]WARNING: [/bold red][bold white]User Terminated Program Before Setup Was Complete: Project '{name}' Has Been Deleted"))



            elif cmd.upper() == "QUIT":
                sys.exit(console.print("[bold cyan]Exiting... bye!"))

            else:
                print("Invalid")

    except Exception as e:
        print(traceback.format_exc())
