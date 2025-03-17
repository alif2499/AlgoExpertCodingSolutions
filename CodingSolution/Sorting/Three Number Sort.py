# Time | O(n) -- Space | O(1)

def threeNumberSort(array, order):
    firstCount = 0
    secondCount = 0
    thirdCount = 0
    for i in range(len(array)):
        if array[i] == order[0]:
            firstCount += 1
        elif array[i] == order[1]:
            secondCount += 1
        elif array[i] == order[2]:
            thirdCount += 1
            
    for i in range(len(array)):
        if i < firstCount:
            array[i] = order[0]
        elif i >= firstCount and i < firstCount + secondCount:
            array[i] = order[1]
        else:
            array[i] = order[2]
    return array