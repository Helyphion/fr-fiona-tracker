import yaml
from rich import print

def getFamiliarsData():
    featsOverview = ""
    featsInstructions = ""

    for x in info["familiars"]:
        
        # excludes the second familiar from input validation
        # (since there are a handful feats that only require one)
        requiredData = x.copy()
        requiredData.pop("req fam 2")

        # creates a list of true/false values based on whether each field the familiar entry is filled in or not
        # ...super condensed though, so it kind of hurts my brain
        filled = [v not in (None, "") for v in requiredData.values()]
        print(filled)

        if all(filled):
            # assembles overview list for start of post, and edit instructions
            featsOverview += f"\n[*][gamedb item={x["feat fam"]}] // [b]{x["source"]}[/b]\n(requires [gamedb item={x["req fam 1"]}] + [gamedb item={x["req fam 2"]}])"
            featsInstructions += f"[rule]\nSearch for: [b]={x["goes after"]}][/b]\n[code]{"{rule}"}\n[gamedb item={x["req fam 1"]}]\n[gamedb item={x["req fam 2"]}][/code]"
        elif any(filled):
            raise Exception(f"Feats data is incomplete.")
        else:
            print("skipped a blank familiars entry")

    return featsOverview, featsInstructions


def spacingInstructions():
    
    ret = ""
    sentenceList = []

    for x in info["spacing"]:

        goesAfter = x["goes after"]
        change = x["change"]

        # equivalent to "if goesAfter == None" (because empty variables evaluate to false)
        if not goesAfter and not change:
            print("skipped a blank spacing entry")
        # raises an exception if any spacing entry specifies only one of goesAfter or Change
        elif not goesAfter or not change:
            raise Exception(f"Spacing data is incomplete. {x}")
        # actual code to be run after the input data is validated to be fine
        else:
            # grammars the sentence correctly lol
            sentenceList.append(f"search for [b]={goesAfter}][/b] and [b]{"add" if change > 0 else "remove"} {abs(change)} {"new" if change > 0 else "blank"} {"line" if abs(change) == 1 else "lines"}[/b] below it")

    # if there are no filled-in entries at all, exits early
    if sentenceList == []:
        return ""
    
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

# opens post template
with open("update-post-template.txt", "r") as file:
    template = file.read()

output = template


announcementURL = info["announcement url"]
FRdate = info["fr date"]
# raises exception if URL or date are missing
if not announcementURL or not FRdate:
    raise Exception("URL/date not provided.")

featNumber = len(info["familiars"])
# assembles and properly grammars first sentence of post
introSentence = f"{featNumber} new Fiona {"familiar" if featNumber == 1 else "familiars"} [url={announcementURL}]{"has" if featNumber == 1 else "have"} been added[/url]."


featsOverview, featsInstructions = getFamiliarsData()

# adds [rule] into bio ver, omits it in forum ver
bioInstructions = featsInstructions.format(rule="[rule]")
forumInstructions = featsInstructions.format(rule="")

# inserts spacing instructions
output = output.replace("--spacing", spacingInstructions())

# optional parts are provided as --placeholder in the template, required ones as {placeholder}
# (as to work correctly with .format(), which insists on replacing all {} it finds)
output = output.format(intro=introSentence, date=FRdate, featsList=featsOverview, bioVer=bioInstructions, forumVer=forumInstructions)

with open("output.txt", "w") as file:
    file.write(output)