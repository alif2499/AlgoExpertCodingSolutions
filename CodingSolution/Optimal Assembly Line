def optimalAssemblyLine(stepDurations, numStations):
    left, right = max(stepDurations), sum(stepDurations)
    maxDuration = float("inf")
    
    while left <= right:
        mid = (left + right) // 2
        if needMoreStation(stepDurations, numStations, mid):
            left = mid + 1
        else:
            maxDuration = mid
            right = mid - 1
    return maxDuration

def needMoreStation(stepDurations, numStations, mid):
    sum = 0
    requiredStation = 1
    for i in stepDurations:
        sum = sum + i
        if sum > mid:
            requiredStation += 1
            sum = i
            
    return requiredStation > numStations
