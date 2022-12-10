def signalsum(file):
    cycle = 1
    signal = 1
    signallist = [20,60,100,140,180,220]
    total = 0
    with open(file) as f:
        content = f.readlines()
        for line in content:
            line = line.strip('\n').split(' ')
            if(line[0]=='noop'):
                cycle +=1
            else:
                cycle +=1
                if(cycle in signallist):
                    total = total + (cycle*signal)
                cycle +=1
                signal += int(line[1])
            if(cycle in signallist):
                    total = total + (cycle*signal)
        return total

def image(file):
    cycle = 0
    signal = 1
    signallist = [40,80,120,160,200,240]
    with open(file) as f:
        content = f.readlines()
        print('#',end='')
        for line in content:
            line = line.strip('\n').split(' ')
            if(line[0]=='noop'):
                cycle +=1
                if(signal-1==(cycle%40) or signal==(cycle%40) or signal+1 == (cycle%40)):
                    print('#',end='')
                else:
                    print('.',end='')
            else:
                cycle +=1
                if(cycle in signallist):
                    print(end='\n')
                if(signal-1==(cycle%40) or signal==(cycle%40) or signal+1 == (cycle%40)):
                    print('#',end='')
                else:
                    print('.',end='')
                cycle +=1
                signal += int(line[1])
                if(signal-1==(cycle%40) or signal==(cycle%40) or signal+1 == (cycle%40)):
                    print('#',end='')
                else:
                    print('.',end='')
            if(cycle in signallist):
                print(end='\n')
        return '' 

print(signalsum("cycle.txt"))
print(image("cycle.txt"))