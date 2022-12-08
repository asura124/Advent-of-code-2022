def visible(file):
    forest = []
    view = 0
    with open(file) as f:
        content = f.readlines()
        for line in content:
            row = []
            line = line.strip('\n')
            for c in line:
                row.append(int(c))
            forest.append(row)
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if(i!=0 and j<=len(forest[0]) and j!=0 and i<=len(forest) and j!=len(forest[0])-1 and i!=len(forest)-1):
                transpose_forest = list(map(list, zip(*forest))) #transpose
                if(max(forest[i][0:j])<forest[i][j]
                or max(forest[i][j+1::])<forest[i][j]
                or max(transpose_forest[j][0:i])<transpose_forest[j][i]
                or max(transpose_forest[j][i+1::])<transpose_forest[j][i]):
                    view +=1
    view = view + (2*len(forest)) + (2*len(forest[0])) -4
    return view


def scenic_score(file):
    forest = []
    view = 1
    largest = 0
    with open(file) as f:
        content = f.readlines()
        for line in content:
            row = []
            line = line.strip('\n')
            #print(line)
            for c in line:
                row.append(int(c))
            forest.append(row)
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            if(i!=0 and j<=len(forest[0]) and j!=0 and i<=len(forest) and j!=len(forest[0])-1 and i!=len(forest)-1):
                view = 1
                transpose_forest = list(map(list, zip(*forest))) #transpose
                temp = 0
                for val in range(len(list(reversed(forest[i][0:j])))):
                    if(list(reversed(forest[i][0:j]))[val]<forest[i][j]):
                        temp +=1
                    else:
                        temp +=1
                        break
                view = view * temp
                temp = 0 
                for val in range(len(forest[i][j+1::])):
                    if(forest[i][j+1::][val]<forest[i][j]):
                        temp +=1
                    else:
                        temp +=1
                        break
                view = view * temp
                temp = 0
                for val in range(len(list(reversed(transpose_forest[j][0:i])))):
                    if(list(reversed(transpose_forest[j][0:i]))[val]<forest[i][j]):
                        temp +=1
                    else:
                        temp +=1
                        break
                view = view * temp
                temp = 0
                for val in range(len((transpose_forest[j][i+1::]))):
                    if((transpose_forest[j][i+1::])[val]<forest[i][j]):
                        temp +=1
                    else:
                        temp +=1
                        break
                view = view * temp
                if(view>largest):
                    largest=view    
    return largest


print(visible("trees.txt"))
print(scenic_score("trees.txt"))