import random
import matplotlib.pyplot as plt
import statistics


def getSecondDoor(doors ,x, y):
    second_choosen_door = -1
    if doors[x] != 1:
        second_choosen_door = y
    if doors[y] != 1:
        if second_choosen_door != -1:
            return random.choice([x, y])
        second_choosen_door = x
    return second_choosen_door

sample_cases = []
outer_counter = 0
while outer_counter < 100: 
    win, inner_counter = 0, 0
    while inner_counter < 100 :
        doors = [0,0,0]

        # randomly get 1 at only one of these doors
        while sum(doors) != 1:
            doors[0] = random.choice([0, 1])
            doors[1] = random.choice([0, 1])
            doors[2] = random.choice([0, 1])
        
        # first door choice
        door = random.choice([0,1,2])
        
        # get second door, skip one of the wrong options
        if door == 0:
            door = getSecondDoor(doors, 1, 2)
        elif door == 1:
            door = getSecondDoor(doors, 0, 2)        
        elif door == 2:
            door = getSecondDoor(doors, 0, 1)

        # if second door choice is correct
        if doors[door] == 1:
            win+=1

        inner_counter +=1

    sample_cases.append(win)
    outer_counter += 1


x = list(range(len(sample_cases)))
plt.plot(x, sample_cases)
plt.xlabel('iterations')
plt.ylabel('Win rate out of 100')
plt.ylim(0, 100) 
plt.show()
print(statistics.mean(sample_cases))

#Observation:  Mean was every time greater than 65
