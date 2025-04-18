def optimalFreelancing(jobs):
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    daySpent = 7 * [0]
    totalValue = 0

    for i in range(len(jobs)):
        # if daySpent <= 7:
        deadline = jobs[i]["deadline"]
        value = jobs[i]["payment"]
        while deadline > 0:
            if deadline > 7:
                deadline = 7
            if daySpent [deadline - 1] == 0:
                daySpent [deadline - 1] = value
                break
            else:
                deadline-=1
    for i in range(7):
        totalValue += daySpent[i]
                
    return totalValue
