def bubbleSort(array):
    counter = 0
    while True:
        isSwap = False
        for i in range(len(array) - 1 - counter):
            if array[i] <= array[i + 1]:
                continue
            else:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSwap = True
        counter += 1
        if not isSwap:
            return array
