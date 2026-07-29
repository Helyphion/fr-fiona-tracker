import sys

try:
    
    with open("owned.txt", "r") as file:
        ownedFams = file.read().splitlines()

    with open("in-progress.txt", "r") as file:
        equippedFams = file.read().splitlines()

except:
    userId = input("Enter your user ID: ")

    if userId.startswith("#"):
        userId = userId[1:]

    if not userId.isdigit():
        sys.exit("Error: User ID needs to be numbers only. (And maybe a hashtag at the start, I accounted for that part.)")


    with open("owned.txt", "w") as file:
        file.write("")

    #with open("in-progress.txt", "w") as file:
    #    file.write("")

    instructions = f"""
//////////////////////////////////////////////////////////////////////////////////////////////////////
FOR MORE READABLE INSTRUCTIONS (BUT WITHOUT CUSTOMISED LINKS), CHECK HERE:
https://github.com/Helyphion/fr-fiona-tracker/blob/main/Tools/Bestiary%20Cross-checker/instructions.md
//////////////////////////////////////////////////////////////////////////////////////////////////////

INSTRUCTIONS:
Open https://www1.flightrising.com/bestiary/{userId}?view=discovered&filter=true&location=hoard&bond_level=not-awakened&limit=60&display=compact,
highlight the full page of familiar names, and copy them into owned.txt. You will need to do this for every page individually.
If you keep any familiars in your vault, you should also check 
https://www1.flightrising.com/bestiary/{userId}?view=discovered&filter=true&location=vault&bond_level=not-awakened&limit=60&display=compact 
and copy them as well. (Just paste them into owned.txt along with the others.)

Then, open https://www1.flightrising.com/bestiary/{userId}?view=discovered&filter=true&location=lair&bond_level=not-awakened&limit=60&display=compact,
highlight all familiar names, and copy them into in-progress.txt.
WARNING: The site does not distinguish between familiars equipped in the lair vs hibernal den - if your only copy of a familiar required for a feat 
is currently equipped on a dragon in the hibernal den (and therefore can't be bonded), the script will still not show it.

If the provided copy of feats-list.txt hasn't yet been updated for new feats, you should open 
https://www1.flightrising.com/forums/gde/3416901#post_58979490, highlight from the first familiar name to the last, and copy it all into feats-list.txt.
Don't worry about the headings and spacers, the script will take care of filtering those out; just make sure not to copy anything before the first 
familiar or after the last.

Once you've completed these steps, run the script again to get your queue of fams to be bonded with! :]

(If you have questions about any of this, feel free to contact Schmelios (#676173) through whatever means is convenient to you!)"""
    
    sys.exit(instructions)

def removeNicknames(list):
    for fam in list:
        if fam[0] == '“':
            list.remove(fam)

def removeBlankLinkes(list):
    while "" in list:
        list.remove("")


removeNicknames(ownedFams)
removeBlankLinkes(ownedFams)

removeNicknames(equippedFams)
removeBlankLinkes(equippedFams)


with open("feats-list.txt", "r") as file:
    featsList = file.read().splitlines()

# remove blank lines
while "" in featsList:
    featsList.remove("")

# remove headings, spacers (_), and notes in parentheses
cleanFeatsList = []
for line in featsList:

    if not line.isupper() and not line[0] == "_":

        if line[-1:] == ")":
            line = line[:line.index("(")-1]

        cleanFeatsList.append(line)
    

for x in cleanFeatsList:
    if x in ownedFams and x not in equippedFams:
        # print(x)
        pass