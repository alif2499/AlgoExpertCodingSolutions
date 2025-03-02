# # binary search method with time complexity of O(log(n))-----> see solution 2 for brute-force
# # iterative approach so space complexity is O(1), if it were recursive, then O(log(n)) for storing the recursive
# # calls in memory

def indexEqualsValue(array):
    return indexValueHelper(array, 0, len(array) - 1)
def indexValueHelper(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == array[mid]:
            if mid - 1 > array[mid - 1]:
                return mid
            elif mid - 1 == array[mid - 1]: # mid - 1 < array[mid - 1] can't be, cause the array is sorted
                end =  mid - 1
            else:    
                return mid
        elif mid > array[mid]:
            start = mid + 1
        else:
            end = mid -1
            

    return -1
