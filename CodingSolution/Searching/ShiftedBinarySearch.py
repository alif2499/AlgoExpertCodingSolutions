def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array)-1)

def shiftedBinarySearchHelper(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        match = array[mid]
        if match == target:
            return mid
        elif array[left] <= match:
            if match > target and array[left] <= target:
                right = mid-1
            else:
                left = mid + 1
        else:
            if match < target and array[right] >= target:
                left = mid + 1
            else:
                right = mid -1 

    return -1