def insertionSort(array):
    for i in range(1, len(array)):
        step = 1
        while i - step >= 0:
            if array[i] < array[i - step]:
                swap(array, i, i - step)
                i -= 1
            else:
                step += 1
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    