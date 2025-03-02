def quickselect(array, k):
    return quickselectHelper(array, k, 0, len(array) - 1)

def quickselectHelper(array, searchIndex, start, end):
    while True:
        if start > end:
            raise Exception("Something is wrong with the code!!")
        if start == end:
            return array[start]
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(array, left, right)
            if array[left] <= array[pivot]:
                left += 1
            if array[right] >= array[pivot]:
                right -= 1
    
        swap(array, pivot, right)
        if right == searchIndex - 1:
            return array[right]
        elif right > searchIndex - 1:
            end =  right - 1
        else:
            start = right + 1
        
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

