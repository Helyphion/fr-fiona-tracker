from rich import print

try:
    with open("update-data.txt", "r") as file:
        info = file.read().splitlines()
except FileNotFoundError:
    with open("update-data.txt", "w") as file:
        file.write("F_ID\nF_Primary\nF_Secondary\nF_Tertiary\n\nM_ID\nM_Primary\nM_Secondary\nM_Tertiary")
    print("[bold yellow]No input.txt found. File has been created; please write your data into it.[/bold yellow]")
    raise