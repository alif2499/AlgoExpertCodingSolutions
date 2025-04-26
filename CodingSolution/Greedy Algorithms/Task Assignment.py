# Time -> O(nlog(n)) --- Space -> O(n)

def taskAssignment(k, tasks):
    sorted_tasks = sorted(tasks)
    output = []
    length = len(tasks)
    for i in range(length - 1, int(length/2) - 1, -1):
        task = [tasks.index(sorted_tasks[i]), tasks.index(sorted_tasks[length - 1 - i])]
        tasks[tasks.index(sorted_tasks[i])] = 0
        tasks[tasks.index(sorted_tasks[length - 1 - i])] = 0
        output.append(task)
    return output
