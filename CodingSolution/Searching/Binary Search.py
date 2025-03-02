def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        match = array[mid]
        if match == target:
            return mid
        elif match > target:
            right =  mid-1
        elif match < target:
            left =  mid+1
            
    return -1
