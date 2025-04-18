def optimalFreelancing(jobs):
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    daySpent = 0
    totalValue = 0

    for i in range(len(jobs)):
        # if daySpent <= 7:
        remaining = jobs[i]["deadline"]
        value = jobs[i]["payment"]
        if remaining > daySpent and daySpent <= 7:
            daySpent += 1
            totalValue += value
                
    return totalValue
