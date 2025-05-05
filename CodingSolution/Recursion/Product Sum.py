# Time -> O(N) || Space -> O(d): where N is the total number of elements including the sub-arrays
# and d is the maximum depth

def productSum(array, depth = 1):
    sum = 0
    for i in range(len(array)):
        if type(array[i]) == list:
            depth += 1
            sum += (depth * productSum(array[i], depth))
            depth = 1
        else:
            sum += array[i]
    return sum