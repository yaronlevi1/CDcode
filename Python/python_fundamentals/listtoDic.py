name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
#favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
favorite_animal = ["horse", "cat", "spider", "giraffe"]

def zipper(a,b):
    if len(a)>=len(b):
        keyList=a 
        valList=b
    else:
        keyList=b
        valList=a 
    new_dict= {}
    for i in range(0,len(keyList)):
        if i<len(valList):
            new_dict[keyList[i]] = valList[i]
        if i>=len(valList):
            new_dict[keyList[i]] = None
    print(new_dict)

zipper(name, favorite_animal)


