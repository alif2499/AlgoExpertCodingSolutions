def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    totalLength = len(arrayOne) + len(arrayTwo)
    if len(arrayOne) <= len(arrayTwo):
        return medianFinder(arrayOne, 0, len(arrayOne) - 1, totalLength, arrayTwo)
    else:
        return medianFinder(arrayTwo, 0, len(arrayTwo) - 1, totalLength, arrayOne)
    return -1

def medianFinder(array, left, right, length, array2):
    while left <= right:
        mid = (left + right) // 2
        firstHalfLength = (mid - left) + 1
        secondHalflength = ((length - 1) // 2) - firstHalfLength
        if array[firstHalfLength - 1] < array2[secondHalflength] and array2[secondHalflength - 1] < array[firstHalfLength]:
            if length % 2 != 0:
                if array[firstHalfLength - 1] >= array2[secondHalflength - 1]:
                    return array[firstHalfLength - 1]
                else:
                    return array2[secondHalflength - 1]
        elif array[firstHalfLength - 1] > array2[secondHalflength]:
            right = mid - 1
        elif array2[secondHalflength - 1] > array[firstHalfLength]:
            left = mid + 1