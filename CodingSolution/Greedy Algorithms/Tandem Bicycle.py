def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    maxTotal = 0
    minTotal = 0
    length = len(redShirtSpeeds)
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        for i in range(length):
            maxTotal += max(redShirtSpeeds[i], blueShirtSpeeds[length - 1 - i])
        return maxTotal
    else:
        for i in range(length):
            minTotal += max(redShirtSpeeds[i], blueShirtSpeeds[i])
        return minTotal
        
