
def most_calories(file):
    elves_calories = []
    total_cal = 0
    with open(file) as f:
        contents = f.readlines()
        for line in contents:
            line = line.strip()
            if(line != ""):
                total_cal += int(line)
            else:
                elves_calories.append(total_cal)
                total_cal = 0
        elves_calories.append(total_cal) 
    max_cal = max(elves_calories)
    return max_cal

def topthreecal(file):
    elves_calories = []
    total_cal = 0
    with open(file) as f:
        contents = f.readlines()
        for line in contents:
            line = line.strip()
            if(line != ""):
                total_cal += int(line)
            else:
                elves_calories.append(total_cal)
                total_cal = 0
        elves_calories.append(total_cal) 
    topthreecal = 0
    for i in range(3):
        topthreecal += max(elves_calories)
        elves_calories.remove(max(elves_calories))
    return topthreecal
        
    

print(most_calories("calories.txt"))
print(topthreecal("calories.txt"))