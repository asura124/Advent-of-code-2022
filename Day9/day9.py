def tailpos(file):
    Head = [0,0]
    Tail = [0,0]
    Tail_visit = {
        (0,0) :1,
    }
    with open(file) as f:
        content = f.readlines()
        for line in content:
            line = line.strip('\n').split(' ')
            for i in range(int(line[1])):
                if(line[0]=='R'):
                    Head[1] +=1
                    if(abs(Tail[1]-Head[1])==2):
                        Tail[1] = Head[1] - 1
                        Tail[0] = Head[0]
                elif(line[0]=='L'):
                    Head[1] -=1
                    if(abs(Tail[1]-Head[1])==2):
                        Tail[1] = Head[1] + 1
                        Tail[0] = Head[0]
                elif(line[0]=='U'):
                    Head[0] +=1
                    if(abs(Tail[0]-Head[0])==2):
                        Tail[0] = Head[0]-1
                        Tail[1] = Head[1]
                elif(line[0]=='D'):
                    Head[0] -=1
                    if(abs(Tail[0]-Head[0])==2):
                        Tail[0] = Head[0]+1
                        Tail[1] = Head[1]
                if(tuple(Tail) not in Tail_visit):
                    Tail_visit[tuple(Tail)] = 1
    return len(Tail_visit)
            

def tailposwithten(file):
    rope =[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    Tail_visit = {
        (0,0) :1,
    }
    with open(file) as f:
        content = f.readlines()
        for line in content:
            line = line.strip('\n').split(' ')
            for i in range(int(line[1])):
                if(line[0]=='R'):
                    rope[0][1] +=1
                elif(line[0]=='L'):
                    rope[0][1] -=1
                elif(line[0]=='U'):
                    rope[0][0] +=1
                elif(line[0]=='D'):
                    rope[0][0] -=1
                for knots in range(len(rope)-1):
                    if(knots==0):
                        if(abs(rope[knots+1][1]-rope[knots][1])==2 and line[0]=='R'):
                            rope[knots+1][1] = rope[knots][1] - 1
                            rope[knots+1][0] = rope[knots][0]
                        elif(abs(rope[knots+1][1]-rope[knots][1])==2 and line[0]=='L'):
                            rope[knots+1][1] = rope[knots][1] + 1
                            rope[knots+1][0] = rope[knots][0]
                        elif(abs(rope[knots+1][0]-rope[knots][0])==2 and line[0]=='U'):
                            rope[knots+1][0] = rope[knots][0]-1
                            rope[knots+1][1] = rope[knots][1]
                        elif(abs(rope[knots+1][0]-rope[knots][0])==2 and line[0]=='D'):
                            rope[knots+1][0] = rope[knots][0]+1
                            rope[knots+1][1] = rope[knots][1]
                    else:
                        if(abs(rope[knots+1][1]-rope[knots][1])==2): #ty - hy
                            if(rope[knots+1][1]>rope[knots][1]):
                                rope[knots+1][1] -=1
                            elif(rope[knots+1][1]<rope[knots][1]):
                                rope[knots+1][1] +=1
                            if(rope[knots+1][0]>rope[knots][0]):
                                rope[knots+1][0] -= 1
                            elif(rope[knots+1][0]<rope[knots][0]):
                                rope[knots+1][0] +=1
                        elif(abs(rope[knots+1][0]-rope[knots][0])==2):
                            if(rope[knots+1][0]<rope[knots][0]):
                                rope[knots+1][0] +=1
                            elif(rope[knots+1][0]>rope[knots][0]):
                                rope[knots+1][0] -= 1
                            if(rope[knots+1][1]>rope[knots][1]):
                                rope[knots+1][1] -=1
                            elif(rope[knots+1][1]<rope[knots][1]):
                                rope[knots+1][1] +=1
                if(tuple(rope[-1]) not in Tail_visit):
                    Tail_visit[tuple(rope[-1])] = 1
    return len(Tail_visit)

print(tailpos("move.txt"))
print((tailposwithten("move.txt")))