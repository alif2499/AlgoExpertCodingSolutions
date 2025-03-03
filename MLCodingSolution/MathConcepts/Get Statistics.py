def get_statistics(input_list):
    mean  = meanCal(input_list)
    median, sorted_list = medianCal(input_list)
    mode = modeCal(sorted_list)
    sample_variance = sampleVarianceCal(mean, input_list)
    sample_std_dev = sampleStdDevCal(sample_variance)
    mean_conf_interval = meanConfIntervalCal(mean, sample_std_dev, input_list)
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_std_dev,
        "mean_confidence_interval": mean_conf_interval,
    }

def meanCal(inlist):
    sum = 0
    for i in inlist:
        sum = sum + i
    return sum / len(inlist)

def medianCal(inlist):
    quickSortHelper(inlist, 0, len(inlist) - 1)
    sorted_list =  inlist
    if len(inlist) % 2 == 0:
        return (sorted_list[len(inlist) // 2] + sorted_list[(len(inlist) // 2) - 1]) / 2, sorted_list
    else:
        return sorted_list[len(inlist) // 2], sorted_list
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

    leftIsSmaller = right - 1 - start < end - (right + 1)
    if leftIsSmaller:
        quickSortHelper(array, start, right - 1)
        quickSortHelper(array, right + 1, end)
    else:
        quickSortHelper(array, right + 1, end)
        quickSortHelper(array, start, right - 1)
    
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def modeCal(inlist):
    dict = {}
    mode = 0
    max_count = 0
    for i in range(len(inlist)):
        count  = 1
        if str(inlist[i]) not in dict.keys():
            while i < len(inlist) - 1 and inlist[i + 1] == inlist[i]:
                count += 1
                i = i + 1
            max_count = count if count >= max_count else max_count
            if max_count == count:
                mode = inlist[i]
            dict[str(inlist[i])] = count
    return mode

def sampleVarianceCal(mean, inlist):
    sum = 0
    for i in range(len(inlist)):
        sq_diff = (inlist[i] - mean) * (inlist[i] - mean)
        sum = sum + sq_diff
    return sum / (len(inlist) - 1)

def sampleStdDevCal(sample_variance):
    return sample_variance ** 0.5

def meanConfIntervalCal(mean, sample_std_dev, input_list):
    std_error = sample_std_dev / (len(input_list) ** 0.5)
    lower = mean - (1.96 * std_error)
    upper = mean + (1.96 * std_error)

    return [lower, upper]