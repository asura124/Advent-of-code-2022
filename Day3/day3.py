

def sumprior(file):
    total = 0
    with open(file) as f:
        contents = f.readlines()
        for l in contents:
            l = l.strip('\n')
            for i in l[0:len(l)//2]:
                if(i in l[len(l)//2::]):
                    if(i.isupper()):
                        total += ord(i) -64 + 26
                    else:
                        total += ord(i) - 96
                    break
        return total

def groupsofthree(file):
    total = 0
    groups = []
    check = False
    with open(file) as f:
        contents = f.readlines()
        for l in contents:
            l = l.strip('\n')
            if(len(groups)==3):
                for i in groups[0]:
                    if(i in groups[1] and i in groups[2]):
                        if(i.isupper() and not check):
                            total += ord(i) -64 + 26
                            check = True
                        elif(i.islower() and not check):
                            total += ord(i) - 96
                            check = True
                groups = []
                groups.append(l)
                check = False
            else:
                groups.append(l)
        if(len(groups)!=0):
            for i in groups[0]:
                if(i in groups[1] and i in groups[2]):
                    if(i.isupper() and not check):
                        total += ord(i) -64 + 26
                        check = True
                    elif(i.islower() and not check):
                        total += ord(i) - 96
                        check = True
        return total

print(sumprior("rucksack.txt"))
print(groupsofthree("rucksack.txt"))