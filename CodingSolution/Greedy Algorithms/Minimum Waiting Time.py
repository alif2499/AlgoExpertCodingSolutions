# time -> O(nlog(n)) || space -> O(1)

def minimumWaitingTime(queries):
    if len(queries) == 1:
        return 0
    queries.sort()
    currWaitTime = 0
    totalWaitTime = 0

    for i in range(len(queries) - 1):
        currWaitTime += queries[i]
        totalWaitTime += currWaitTime
    return totalWaitTime
