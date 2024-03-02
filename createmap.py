import numpy as np
startpoint = 0
def generatemap():
    
    map = np.random.randint(0, 2, size=(4, 4))#creates random 4x4 map contains 1s and 0s 
    if validations(map):
        startpoint = find_start_point(map)
        return map,startpoint
    else:
        return generatemap()
    
def find_start_point(map):
    for i in range(4):
        if map[0][i] == 1:
            return i
    return None

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


