import yaml
# from rich import print

def getFamiliarsData():
    ret = []

    for x in info["familiars"]:
        # print(x.values())

        filled = []
        for v in x.values():
            if v not in (None, ""):
                filled.append(True)
            else:
                filled.append(False)
        print(filled)


def spacingInstructions():
    
    ret = ""
    sentenceList = []

    for x in info["spacing"]:

        goesAfter = x["goes after"]
        change = x["change"]

        # equivalent to "if goesAfter == None" (because empty variables evaluate to false)
        if not goesAfter and not change:
            print("skipped blank spacing entry")
        # raises an exception if any spacing entry specifies only one of goesAfter or Change
        elif not goesAfter or not change:
            raise Exception(f"Spacing data is incomplete. {x}")
        # actual code to be run after the input data is validated to be fine
        else:
            # grammars the sentence correctly lol
            sentenceList.append(f"search for [b]={goesAfter}][/b] and [b]{"add" if change > 0 else "remove"} {abs(change)} {"new" if change > 0 else "blank"} {"line" if abs(change) == 1 else "lines"}[/b] below it")

    lastEntry = sentenceList[len(sentenceList)-1]

    for x in sentenceList:
        if x == lastEntry:
            ret += x + "."
        else:
            ret += x + ";\n"
    
    ret = "[rule]\nAdditionally, to align the columns correctly, you will have to:\n" + ret

    return ret



# checks if update-data.yaml exists, creates it if not
try:
    with open("update-data.yaml", "r") as file:
        info = yaml.safe_load(file)
except FileNotFoundError:
    with open("update-data.yaml", "w") as file:
        file.write('announcement url: \nfr date: \n\nspacing:\n  - goes after: \n    change: \n  - goes after: \n    change: \n\nfamiliars:\n  - feat fam: \n    req fam 1: \n    req fam 2: \n    source: \n    goes after: \n\n  - feat fam: \n    req fam 1: \n    req fam 2: \n    source: \n    goes after: ')
    print("[bold yellow]No update-data.yaml found. File has been created; please write your data into it.[/bold yellow]")
    raise

with open("update-post-template.txt", "r") as file:
    template = file.read()

announcementURL = info["announcement url"]
FRdate = info["fr date"]
if not announcementURL or not FRdate:
    raise Exception("URL/date not provided.")

"{featNumber} new Fiona familiars [url={URL}]have been added[/url]."
print(len(info["familiars"]))

getFamiliarsData()

# only runs this part if spacing section has entries
if info["spacing"]:
    spacingInstructions()

test = template.format(URL=announcementURL, featNumber=3, date=FRdate)
# print(test)

# dude idk what happened but my vscode broke and just would not recognise my python installation as a valid interpreter and I was losing my mind for like an hour trying to fix it
# and now it works again and I ??? don't know why ?????
# this is why you don't code at 3am...