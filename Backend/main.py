import random
from src.nameData import FirstNames_Masc_UK , FirstNames_Fem_UK, LastNames__UK

ORDER = 5

def buildModel(markov: dict, nameData: list):
    for name in nameData:
        prefix = "_" * ORDER
        name = prefix + str(name).lower() + "*"
        for i in range(len(name) - ORDER):
            pre = name[i : i+ORDER]
            nextChar = name[i+ORDER]
            if pre not in markov.keys():
                markov[pre] = list()
            
            markov[pre].append(nextChar)
            

def generateName(markov:dict, limit :int = 0):
    name = ""
    prefix = "_" * ORDER
    nextChar = ""
    
    #initializing
    nextChar = random.choice(markov[prefix])
    if nextChar != "*":
        name += nextChar
    
    prefix = prefix[1:] + nextChar
    
    #name loop
    
    if limit > 0:
        while(nextChar != "*" and len(name) < limit):
                if prefix in markov.keys():
                    nextChar = random.choice(markov[prefix])
                    if nextChar != "*":
                        name += nextChar
                    prefix = prefix[1:] + nextChar
            
    else:
        while(nextChar != "*"):
            if prefix in markov.keys():
                nextChar = random.choice(markov[prefix])
                if nextChar != "*":
                    name += nextChar
                prefix = prefix[1:] + nextChar
    return name

def getFNameList(model, namelist:list, length:int, limit =0):
    namelist = []
    for i in range(length):
        name = generateName(model, limit)
        name = name[0].upper() + name[1:]
        if name in namelist:
            i -= 1
        else:    
            namelist.append(name)
    return namelist

def getLNameList(model, namelist:list, length:int, limit =0):
    namelist = []
    for i in range(length):
        name = generateName(model, limit)
        name = name[0].upper() + name[1:]
        if name.upper() in namelist:
            i -= 1
        else:    
            namelist.append(name)
    return namelist


def getNameList(model, namelist:list, length:int, limit =0):
    namelist = []
    for i in range(length):
        name = generateName(model, limit)
        name = name[0].upper() + name[1:]  
        namelist.append(name)
    return namelist

if __name__ == "__main__":
    markov_Fmasc = dict()
    makrov_Ffem = dict()
    makrov_L = dict()
    buildModel(markov_Fmasc, FirstNames_Masc_UK)
    buildModel(makrov_Ffem, FirstNames_Fem_UK)
    buildModel(makrov_L, LastNames__UK)

    fnames = getFNameList(markov_Fmasc,FirstNames_Masc_UK,10,7)
    #fnames = getNameList(makrov_Ffem,FirstNames_Fem_UK,10,7)
    lnames = getLNameList(makrov_L, LastNames__UK, 10, 10)
    
    for f, l in zip(fnames, lnames):
        print(f"{f} {l}")