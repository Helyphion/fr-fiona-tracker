# awakened
#  https://www1.flightrising.com/bestiary/676173/1?view=all&filter=true&location=&bond_level=awakened&name=&sort=name_asc&limit=60&display=compact

# in progress
# https://www1.flightrising.com/bestiary/676173?view=all&filter=true&location=lair&bond_level=not-awakened&name=&sort=name_asc&limit=60&display=compact

# feats list
# https://www1.flightrising.com/forums/gde/3416901#post_58979490


with open("awakened.txt", "r") as file:
    awakenedFams = file.read().splitlines()


# remove nicknames from awakened list
for fam in awakenedFams:
    if fam[0] == '“':
        awakenedFams.remove(fam)



with open("in-progress.txt", "r") as file:
    equippedFams = file.read().splitlines()

# remove nicknames from equipped list
for fam in equippedFams:
    if fam[0] == '“':
        equippedFams.remove(fam)



with open("feats-list.txt", "r") as file:
    featsList = file.read().splitlines()


# remove blank lines
while "" in featsList:
    featsList.remove("")


for line in featsList:

    if line.isupper():
        featsList.remove(line)

    elif line[0] == "_":
        featsList.remove(line)

    elif line[-1:] == ")":
        currentLine = featsList.index(line)
        featsList[currentLine] = line[:line.index("(")-1]
    

print(featsList)
