def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while right >= left:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]: 
            right -= 1
            
    swap(array, right, pivot)

    leftIsSmaller = (right - 1) - start < end - (right + 1)
    if leftIsSmaller:
        quickSortHelper(array, start, right - 1)
        quickSortHelper(array, right + 1, end)
    else:
        quickSortHelper(array, right + 1, end)
        quickSortHelper(array, start, right - 1)
    
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]