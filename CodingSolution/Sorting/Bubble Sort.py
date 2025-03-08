def bubbleSort(array):
    while True:
        isSwap = False
        for i in range(len(array) - 1):
            if array[i] <= array[i + 1]:
                continue
            else:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSwap = True
        if not isSwap:
            return array
