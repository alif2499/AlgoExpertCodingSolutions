# # time = O(n)

# def searchForRange(array, target):
#     return searchRangeHelper(array, target, 0, len(array)-1)
# def searchRangeHelper(array, target, left, right):
#     while left <= right:
#         mid = (left + right) // 2
#         potentialMatch = array[mid]
#         if potentialMatch == target:
#             start = mid
#             end = mid 
#             while start >= 0:
#                 if array[start] == target:
#                     start -= 1
#                 else:
#                     break
#             while end <= len(array)-1:
#                 if array[end] == target:
#                     end += 1
#                 else:
#                     break
#             return [start+1, end-1]
#         elif potentialMatch < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return [-1, -1]


# time = O(log(n))
def searchForRange(array, target):
    output = [-1, -1]
    searchForRangeHelper(array, target, 0, len(array)-1, output, True)
    searchForRangeHelper(array, target, 0, len(array)-1, output, False)
    return output

def searchForRangeHelper(array, target, left, right, output, goLeft):
    while left <= right:
        mid = (left + right) // 2
        potMatch = array[mid]
        if target < potMatch:
            right = mid - 1
        elif target > potMatch:
            left = mid + 1
        else: # when the mid value matches the target value
            if goLeft:
                if mid == 0 or array[mid - 1] != target: # will enter only once then exits the function
                    output[0] = mid
                    return
                else:
                    right = mid - 1 # if the matched mid value is not the first index
            else:
                if mid == len(array)-1 or array[mid + 1] != target: # will enter only once then exits the function
                    output[1] = mid
                    return
                else:
                    left = mid + 1 # if the matched mid value is not the last index

