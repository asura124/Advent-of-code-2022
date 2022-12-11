
def lvlofbussiness(file):
    with open(file) as f:
        monkeys = {0 :[],1 :[], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],}
        operations = {}
        test = {0 :[], 1 :[], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],}
        inspection = {0 :0, 1 :0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,}
        content = f.readlines()
        count = 0
        line_count = 1
        for line in content:
            line = line.strip('\n').split(' ')
            if(line_count%7==0):
                count +=1
            elif(line_count%7==1):
                pass
            elif(line_count%7==2):
                for i in line[line.index('items:')+1::]:
                    monkeys[count].append(int(i.strip(',')))
            elif(line_count%7==3):
                if(count not in operations) : operations[count] = (line[-2::])
            else:
                test[count].append(int(line[-1]))
            line_count+=1
        for i in range(20):
            for mkey in monkeys:
                length = len(monkeys[mkey])
                inspection[mkey] += length
                for item in range(length):
                    temp = monkeys[mkey][0]
                    if(operations[mkey][0]=='+'):
                        if(operations[mkey][1]=='old'):
                            temp = temp + temp
                        else:
                            temp = temp + int(operations[mkey][1])
                        temp = temp//3
                    else:
                        if(operations[mkey][1]=='old'):
                            temp = temp * temp
                        else:
                            temp = temp * int(operations[mkey][1])
                        temp = temp//3
                    monkeys[mkey].pop(0)
                    if(temp%test[mkey][0]==0):
                        monkeys[test[mkey][1]].append(temp)
                    else:
                        monkeys[test[mkey][2]].append(temp)
        return sorted(inspection.values())[-2] * sorted(inspection.values())[-1]

def lvlofbussiness10000(file):
    with open(file) as f:
        monkeys = {0 :[],1 :[], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],}
        operations = {}
        test = {0 :[], 1 :[], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],}
        inspection = {0 :0, 1 :0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,}
        content = f.readlines()
        count = 0
        line_count = 1
        for line in content:
            line = line.strip('\n').split(' ')
            if(line_count%7==0):
                count +=1
            elif(line_count%7==1):
                pass
            elif(line_count%7==2):
                for i in line[line.index('items:')+1::]:
                    monkeys[count].append(int(i.strip(',')))
            elif(line_count%7==3):
                if(count not in operations) : operations[count] = (line[-2::])
            else:
                test[count].append(int(line[-1]))
            line_count+=1
        div =1
        for i in test:
            div = div * test[i][0]
        for i in range(10000):
            for mkey in monkeys:
                length = len(monkeys[mkey])
                inspection[mkey] += length
                for item in range(length):
                    temp = monkeys[mkey][0]
                    if(operations[mkey][0]=='+'):
                        if(operations[mkey][1]=='old'):
                            temp = temp + temp
                        else:
                            temp = temp + int(operations[mkey][1])
                    else:
                        if(operations[mkey][1]=='old'):
                            temp = temp * temp
                        else:
                            temp = temp * int(operations[mkey][1])
                    monkeys[mkey].pop(0)
                    if(temp%test[mkey][0]==0):
                        monkeys[test[mkey][1]].append(temp%div)
                    else:
                        monkeys[test[mkey][2]].append(temp%div)
        return sorted(inspection.values())[-2] * sorted(inspection.values())[-1]
            

print(lvlofbussiness("movement.txt"))
print(lvlofbussiness10000("movement.txt"))
