def findThreeLargestNumbers(array):
    output = [None, None, None]
    for i in range(len(array)):
        if output[2] is None or array[i] > output[2]:
            updateValue(output, array, i, 0, 2)
        elif output[1] is None or array[i] > output[1]:
            updateValue(output, array, i, 0, 1)
        elif output[0] is None or array[i] > output[0]:
            updateValue(output, array, i, 0, 0)

    return output

def updateValue(output, array, i, k, j):
    while k < j:
        output[k] = output[k+1]
        k += 1
    output[j] = array[i]