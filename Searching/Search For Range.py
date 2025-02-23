def searchForRange(array, target):
    return searchRangeHelper(array, target, 0, len(array)-1)
def searchRangeHelper(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        potentialMatch = array[mid]
        if potentialMatch == target:
            start = mid
            end = mid 
            while start >= 0:
                if array[start] == target:
                    start -= 1
                else:
                    break
            while end <= len(array)-1:
                if array[end] == target:
                    end += 1
                else:
                    break
            return [start+1, end-1]
        elif potentialMatch < target:
            left = mid + 1
        else:
            right = mid - 1
    return [-1, -1]
