# owned
# already excludes awakened ones
# https://www1.flightrising.com/bestiary/676173?view=discovered&filter=true&location=&bond_level=not-awakened&name=&sort=name_asc&limit=60&display=compact

# or.. hoard
# https://www1.flightrising.com/bestiary/676173/1?view=discovered&filter=true&location=hoard&bond_level=not-awakened&name=&sort=name_asc&limit=60&display=compact
# + vault
# https://www1.flightrising.com/bestiary/676173?view=discovered&filter=true&location=vault&bond_level=not-awakened&name=&sort=name_asc&limit=60&display=compact
# ? would make the in progress check obsolete, might be smarter..
# neeevermind, duplicates still show up. so not obsolete; but still less to copy if going with these two links

# in progress
# https://www1.flightrising.com/bestiary/676173?view=all&filter=true&location=lair&bond_level=not-awakened&name=&sort=name_asc&limit=60&display=compact

# feats list
# https://www1.flightrising.com/forums/gde/3416901#post_58979490

# TODO: clean up links


def removeNicknames(list):
    for fam in list:
        if fam[0] == '“':
            list.remove(fam)

with open("owned.txt", "r") as file:
    ownedFams = file.read().splitlines()

with open("in-progress.txt", "r") as file:
    equippedFams = file.read().splitlines()

removeNicknames(ownedFams)
removeNicknames(equippedFams)



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
        print(x)