"""
A,X = Rock (1)
B,Y = Paper (2)
C,Z = Scissor (3)

Loss = 0
Draw = 3
win = 6
"""
def score(file):
    strat={
        "A X" : 4,
        "A Y" : 8,
        "A Z" : 3,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 7,
        "C Y" : 2,
        "C Z" : 6, 
    }
    totalpoints = 0
    with open(file) as f:
        contents = f.readlines()
        for l in contents:
            l = l.strip('\n')
            totalpoints += strat[l]
    return totalpoints

"""
A = Rock (1)
B = Paper (2)
C = Scissor (3)

X = lose (0)
Y = draw (3)
Z = win (6)
"""
def modifiedscore(file):
    strat={
        "A X" : 3,
        "A Y" : 4,
        "A Z" : 8,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 2,
        "C Y" : 6,
        "C Z" : 7, 
    }
    totalpoints = 0
    with open(file) as f:
        contents = f.readlines()
        for l in contents:
            l = l.strip('\n')
            totalpoints += strat[l]
    return totalpoints

print(score("rps.txt"))
print(modifiedscore("rps.txt"))