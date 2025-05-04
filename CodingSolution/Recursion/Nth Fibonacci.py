# time -> O(n) || space -> O(1)

def getNthFib(n):
    F1 = 0
    F2 = 1
    start = 3
    if n == 1:
        return F1
    if n == 2:
        return F2
    if n > 2:
        while start <= n:
            temp = F1
            F1 = F2
            F2 += temp
            start += 1
        return F2
    pass
