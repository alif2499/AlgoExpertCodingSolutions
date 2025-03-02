# O(log(min(n,m))) time | O(1) space

def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    totalLength = len(arrayOne) + len(arrayTwo)
    if len(arrayOne) <= len(arrayTwo):
        return medianFinder(arrayOne, 0, len(arrayOne) - 1, totalLength, arrayTwo)
    else:
        return medianFinder(arrayTwo, 0, len(arrayTwo) - 1, totalLength, arrayOne)
    return -1

def medianFinder(array, left, right, length, array2):
    while True:
        mid = (left + right) // 2
        firstHalfLength = mid + 1
        secondHalflength = ((length - 1) // 2) - firstHalfLength + 1

        smallMaxLeft = array[firstHalfLength - 1] if (firstHalfLength - 1) >= 0 else float("-inf")
        smallMinRight = array[firstHalfLength] if firstHalfLength < len(array) else float("inf")
        bigMaxLeft = array2[secondHalflength - 1] if (secondHalflength - 1) >= 0 else float("-inf")
        bigMinRight = array2[secondHalflength] if secondHalflength < len(array2) else float("inf")

        if smallMaxLeft > bigMinRight:
            right = mid - 1
        elif bigMaxLeft > smallMinRight:
            left = mid + 1
        else:
            if length % 2 != 0:
                return max(smallMaxLeft, bigMaxLeft)
            else:
                return (max(smallMaxLeft, bigMaxLeft) + min(smallMinRight, bigMinRight)) / 2
        
