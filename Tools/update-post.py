import yaml
from rich import print


try:
    with open("update-data.yaml", "r") as file:
        info = yaml.safe_load(file)
except FileNotFoundError:
    with open("update-data.yaml", "w") as file:
        file.write('announcement url: \nfr date: \n\nspacing:\n  - goes after: \n    change: \n  - goes after: \n    change: \n\nfamiliars:\n  - feat fam: \n    req fam 1: \n    req fam 2: \n    source: \n    goes after: \n\n  - feat fam: \n    req fam 1: \n    req fam 2: \n    source: \n    goes after: ')
    print("[bold yellow]No update-data.yaml found. File has been created; please write your data into it.[/bold yellow]")
    raise


announcementURL = info["announcement url"]
FRdate = info["fr date"]

spacing = []

# add handling for when there's no spacing updates 
for x in info["spacing"]:

    goesAfter = x["goes after"]
    change = x["change"]

    # equivalent to "if goesAfter == None" (because empty variables evaluate to false)
    if not goesAfter and not change:
        print("skip this entry")
    # raises an exception if any spacing entry specifies only one of goesAfter or Change
    elif not goesAfter or not change:
        raise Exception(f"Data in update-data.yaml is incomplete. {x}")
    # actual code to be run after the input data is validated to be fine
    else:
        # grammars the sentence correctly lol
        spacing.append(f"search for [b]={goesAfter}][/b] and {"add" if change > 0 else "remove"} [b]{abs(change)} blank {"line" if abs(change) == 1 else "lines"}[/b] below it")
        print(spacing)

# note bc I will forget: spacing variable contains the sentences for spacing instructions; need to add punctuation

# dude idk what happened but my vscode broke and just would not recognise my python installation as a valid interpreter and I was losing my mind for like an hour trying to fix it
# and now it works again and I ??? don't know why ?????
# this is why you don't code at 3am...