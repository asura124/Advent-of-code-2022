def sumdir(file):
    filesystem = {}
    #currpath = []
    currpath = ''
    with open(file) as f:
        content = f.readlines()
        for l in content:
            l = l.strip('\n').strip('$ ').split(' ')
            if(len(l)==2 and l[0]=='cd'):
                if(currpath+l[1] not in filesystem and l[1]!='..'):
                    filesystem[currpath+'/'+l[1]] = []
                    currpath = currpath + '/' + l[1]
                else:
                    if(l[1]=='..'):
                        currpath = currpath[0:currpath.rfind('/')]
                    else:
                        currpath = currpath + '/' + l[1]
            elif(len(l)==2 and l[0]=='dir'):
                filesystem[currpath].append(currpath+ '/'+l[1])
                filesystem[currpath + '/' + l[1]] = []
            elif(len(l)==2 and l[0]!='cd'):
                filesystem[currpath].append((l[1],l[0]))
    sum_dir = 0
    for dir in filesystem:
        if(sum(dir,filesystem)<=100000):
            sum_dir += sum(dir,filesystem)
    return sum_dir

def sum(dir,dict):
    total = 0
    for i in dict[dir]:
        if(isinstance(i,tuple)):
            total += int(i[1])
        else:
            total += sum(i,dict)
    return total

def deletedirsize(file):
    filesystem = {}
    #currpath = []
    currpath = ''
    with open(file) as f:
        content = f.readlines()
        for l in content:
            l = l.strip('\n').strip('$ ').split(' ')
            if(len(l)==2 and l[0]=='cd'):
                if(currpath+l[1] not in filesystem and l[1]!='..'):
                    filesystem[currpath+'/'+l[1]] = []
                    currpath = currpath + '/' + l[1]
                else:
                    if(l[1]=='..'):
                        currpath = currpath[0:currpath.rfind('/')]
                    else:
                        currpath = currpath + '/' + l[1]
            elif(len(l)==2 and l[0]=='dir'):
                filesystem[currpath].append(currpath+ '/'+l[1])
                filesystem[currpath + '/' + l[1]] = []
            elif(len(l)==2 and l[0]!='cd'):
                filesystem[currpath].append((l[1],l[0]))
    totalused = sum('//',filesystem)
    spaceneeded = totalused-40000000
    smallest = 7000000
    for dir in filesystem:
        if(spaceneeded-sum(dir,filesystem)<0 and sum(dir,filesystem)<smallest):
            smallest = sum(dir,filesystem)
    return smallest


print(sumdir("system.txt"))
print(deletedirsize("system.txt"))