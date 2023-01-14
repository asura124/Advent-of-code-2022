def shortest(file):
    visited = {}
    grid = [[]]
    steps = 0
    with open(file) as f:
        content = f.readlines()
        for line in content:
            line = line
            for l in line:
                if(l=='\n'):
                    grid.append([])
                else:
                    grid[-1].append(l)
        startingrow = 0
        startingcol = 0
        endingrow = 0
        endingcol = 0
        grid.pop()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]=='S'):
                    startingrow=i
                    startingcol=j
                    grid[i][j]='a'
                elif(grid[i][j]=='E'):
                    endingrow=i
                    endingcol = j
                    grid[i][j] = 'z'
        return path(grid,visited,startingrow,startingcol,endingrow,endingcol)

def path(grid,visited,startrow,startcol,endrow,endcol):
    queue = [(startrow,startcol)]
    visited = {}
    distance = 0
    while(len(queue)!=0):
        temp_len = len(queue)
        #print(queue)
        for i in range(temp_len):
            row = queue[i][0]
            col = queue[i][1]
            if(row+1>=0 and row+1<len(grid) and (row+1,col) not in visited):
                if(ord(grid[row+1][col])<=ord(grid[row][col])+1):
                    if((row+1,col) not in queue):
                        queue.append((row+1,col))
            if(row-1>=0 and row-1<len(grid) and (row-1,col) not in visited):
                if(ord(grid[row-1][col])<=ord(grid[row][col])+1):
                    if((row-1,col) not in queue):
                        queue.append((row-1,col))
            if(col+1>=0 and col+1<len(grid[0]) and (row,col+1) not in visited):
                if(ord(grid[row][col+1])<=ord(grid[row][col])+1):
                    if((row,col+1) not in queue):
                        queue.append((row,col+1))
            if(col-1>=0 and col-1<len(grid[0]) and (row,col-1) not in visited):
                if(ord(grid[row][col-1])<=ord(grid[row][col])+1):
                    if((row,col-1) not in queue):
                        queue.append((row,col-1))
            visited[(row,col)] = 1
        distance +=1
        if((endrow,endcol) in queue):
            return distance
        for i in range(temp_len):
            queue.pop(0)
    return len(grid) * len(grid[0])


def feweststeps(file):
    visited = {}
    grid = [[]]
    steps = 0
    with open(file) as f:
        content = f.readlines()
        for line in content:
            line = line
            for l in line:
                if(l=='\n'):
                    grid.append([])
                else:
                    grid[-1].append(l)
        startingrow = 0
        startingcol = 0
        endingrow = 0
        endingcol = 0
        steps_arr = []
        grid.pop()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]=='S'):
                    grid[i][j]='a'
                elif(grid[i][j]=='E'):
                    endingrow=i
                    endingcol = j
                    grid[i][j] = 'z'
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]=='a'):
                    count +=1
                    steps_arr.append(path(grid,visited,i,j,endingrow,endingcol))
        return min(steps_arr)

        

print(shortest("shortest.txt"))
print(feweststeps("shortest.txt"))
