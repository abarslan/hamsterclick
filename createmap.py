import numpy as np

def generatemap():
    map = np.random.randint(0, 2, size=(4, 4))#creates random 4x4 map contains 1s and 0s 
    if validations(map):
        return map
    else:
        return generatemap()

def validations(map): #validates if it is a valid map
    initial = None
    valid = True
    for i in range(4):
        if map[0][i] == 1:
            initial = i
            break

    if initial is None:
        valid = False
    else:
        for j in range(3):
            for k in range(4):
                if map[j+1][k] == 1 and abs(k-initial) > 1:
                    valid = False
                    break
                elif map[j+1][k] == 1:
                    initial = k
                    break
                elif k == 3:
                    valid = False

            if not valid:
                break

    return valid


