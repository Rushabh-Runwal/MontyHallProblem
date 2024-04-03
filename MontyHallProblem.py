import random
import matplotlib.pyplot as plt

def getSecondDoor(doors ,x, y):
    res = -1
    if doors[x] != 1:
        res = y
    if doors[y] != 1:
        if res != -1:
            return random.choice([x, y])
        res = x
    
    return res

sample = []
C = 0
while C < 100: 
    win, cnt = 0, 0
    while cnt < 100 :
        doors = [0,0,0]
        while sum(doors) != 1:
            doors[0] = random.choice([0, 1])
            doors[1] = random.choice([0, 1])
            doors[2] = random.choice([0, 1])

        door = random.choice([0,1,2])
        if door == 0:
            door = getSecondDoor(doors, 1, 2)
        elif door == 1:
            door = getSecondDoor(doors, 0, 2)        
        elif door == 2:
            door = getSecondDoor(doors, 0, 1)

        if doors[door] == 1:
            win+=1

        cnt +=1
    sample.append(win)
    C += 1


x = list(range(len(sample)))
plt.plot(x, sample)
plt.xlabel('iterations')
plt.ylabel('Win rate out of 100')
plt.ylim(0, 100) 
plt.show()
