import json


with open("req-ids.txt", "r") as file:
    reqIds = file.read().splitlines()

with open("req-names.txt", "r") as file:
    reqNames = file.read().splitlines()


output = {}
currentFeat = ""
featCount = 0
currentLine = 0

for line in reqNames:
    famName = ""
    sourceNote = ""

    if line != "":
    
        if line.isupper():
            currentSource = line.title()
        else:

            parenthesis = False
            for char in line:
                    
                if char == "(":
                    parenthesis = True
                    famName = famName.strip() # remove trailing space
                    sourceNote += " " # ...add a space for convenience. yes, ironic
                
                if parenthesis:
                    sourceNote += char
                else:
                    famName += char
            
            famId = ""
            for char in reqIds[currentLine]:
                if char.isnumeric():
                    famId += char
                elif char == "(":
                    break # ensures potential numbers in the parenthesis aren't added to the id
            

            output[currentFeat]["requires"][famName] = {"id": int(famId), "source": currentSource + sourceNote}



    else:
        currentFeat = f"fam {featCount}"
        output[currentFeat] = {"id": 666666, "requires": {}}
        featCount += 1
    
    currentLine += 1



jsonOutput = json.dumps(output, indent=4)

with open("output.txt", "w") as file:
    file.write(jsonOutput)