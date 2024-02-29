import numpy as np
def createmap():
    map = np.random.randint(0, 2, size=(4, 4))
    validations(map)
    print(map)

def validations(map):
    for i in range(4):
        if map[3][i] == 1:
            initial = i
            break
    for j in range(4):
        for k in range(4):
            if map[j][k] == 1 and abs(k-initial)>1 :
                createmap
            elif map[j][k] == 1 :
                initial = k
                break    

createmap()
