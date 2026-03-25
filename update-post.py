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


announcementURL = info["announcement url"]
FRdate = info["fr date"]

spacing = info["spacing"]
familiars = info["familiars"]

print(announcementURL)
print(FRdate)
print(spacing)
print(familiars)
# check number of entries using len(familiars) etc
# also disregard entries with blank (None) fields just in case
# then assemble BBCode list by iterating based on the number of valid entries