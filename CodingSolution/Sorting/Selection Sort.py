def selectionSort(array):
    for j in range(len(array) - 1):
        small = j
        for i in range(j + 1, len(array)):
            if array[i] < array[small]:
                small = i 
            
        swap(array, j, small)
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]