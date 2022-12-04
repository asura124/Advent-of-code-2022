
def contain(file):
    count = 0
    with open(file) as f:
        content = f.readlines()
        for l in content:
            l = l.strip('\n').split(',')
            num1 = l[0].split('-')[0]
            num2 = l[0].split('-')[1]
            num3 = l[1].split('-')[0]
            num4 = l[1].split('-')[1]
            if((int(num1)>=int(num3) and int(num2)<=int(num4)) or (int(num1)<=int(num3) and int(num2)>=int(num4))):
                count +=1
    return count

def overlap(file):
    count = 0
    with open(file) as f:
        content = f.readlines()
        for l in content:
            l = l.strip('\n').split(',')
            num1 = l[0].split('-')[0]
            num2 = l[0].split('-')[1]
            num3 = l[1].split('-')[0]
            num4 = l[1].split('-')[1]
            if((int(num1)>=int(num3) and int(num1)<=int(num4)) or (int(num2)<=int(num3) and int(num2)>=int(num4)) or (int(num3)>=int(num1) and int(num3)<=int(num2)) or (int(num4)<=int(num2) and int(num4)>=int(num1))):
                count +=1
    return count

print(contain("sections.txt"))
print(overlap("sections.txt"))