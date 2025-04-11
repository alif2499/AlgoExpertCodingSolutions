# time -> O(nlog(n)) || space -> O(1)

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    flag = False
    if redShirtHeights[0] < blueShirtHeights[0]:
        flag = True
        for i in range(1, len(redShirtHeights)):
            if redShirtHeights[i] < blueShirtHeights[i]:
                flag = True
            else:
                flag = False
                return flag
    elif redShirtHeights[0] > blueShirtHeights[0]:
        flag = True
        for i in range(1, len(redShirtHeights)):
            if redShirtHeights[i] > blueShirtHeights[i]:
                flag = True
            else:
                flag = False
                return flag
    return flag
