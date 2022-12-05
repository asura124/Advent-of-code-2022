
def stacktop(file):
    seperate = False
    stacks = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    with open(file) as f:
        contents = f.readlines()
        for l in contents:
            l = l.strip('\n')
            l += " "
            stacknum = 1
            if(l!=' ' and not seperate):
                for i in range(0,len(l),4):
                    if(l[i:i+4].strip()!=''):
                        if(not l[i:i+4].strip(' ').isnumeric()):
                            stacks[stacknum].insert(0,l[i:i+4])
                    stacknum +=1
            elif(seperate):
                l = l.split(' ')
                for num in range(int(l[1])):
                    temp = stacks[int(l[3])][-1]
                    stacks[int(l[5])].append(temp)
                    stacks[int(l[3])].pop()
            else:
                seperate = True
    top = ""
    for x in stacks:
        top += stacks[x][-1]
    return top



def crane(file):
    seperate = False
    stacks = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    with open(file) as f:
        contents = f.readlines()
        for l in contents:
            l = l.strip('\n')
            l += " "
            stacknum = 1
            if(l!=' ' and not seperate):
                for i in range(0,len(l),4):
                    if(l[i:i+4].strip()!=''):
                        if(not l[i:i+4].strip(' ').isnumeric()):
                            stacks[stacknum].insert(0,l[i:i+4])
                    stacknum +=1
            elif(seperate):
                l = l.split(' ')
                temp = stacks[int(l[3])][-int(l[1]):]
                stacks[int(l[3])] = stacks[int(l[3])][0:-int(l[1])]
                stacks[int(l[5])] = stacks[int(l[5])] + temp
            else:
                seperate = True
    top = ""
    for x in stacks:
        top += stacks[x][-1]
    return top


print(stacktop("crate.txt"))
print(crane("crate.txt"))



