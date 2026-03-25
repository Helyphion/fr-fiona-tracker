import yaml
from rich import print


try:
    with open("update-data.yaml", "r") as file:
        info = yaml.safe_load(file)
except FileNotFoundError:
    with open("update-data.yaml", "w") as file:
        file.write('announcement url: \nfr date: \n\nspacing:\n  - goes after: ""\n    change: ""\n  - goes after: ""\n    change: ""\n\nfamiliars:\n  - feat fam: \n    req fam 1: \n    req fam 2: \n    source: \n    goes after: \n\n  - feat fam: \n    req fam 1: \n    req fam 2: \n    source: \n    goes after: ')
    print("[bold yellow]No update-data.yaml found. File has been created; please write your data into it.[/bold yellow]")
    raise

