def firstmarker(file):
    with open(file) as f:
        content = f.read()
        content = content.strip('\n')
        for i in range(len(content)-3):
            packet = len(set(content[i:i+4]))
            if(packet==4):
                return i+4

def firstmessage(file):
    with open(file) as f:
        content = f.read()
        content = content.strip('\n')
        for i in range(len(content)-13):
            packet = len(set(content[i:i+14]))
            if(packet==14):
                return i+14


print(firstmarker("packet.txt"))
print(firstmessage("packet.txt"))