# time-> O(n) || space-> O(1)

def validStartingCity(distances, fuel, mpg):
    fuelLeftList = []
    fuelLeft = 0
    for i in range(0, len(distances)):
        fuelLeftList.append(fuelLeft)
        print(fuelLeftList)
        fuelLeft = ((mpg * fuel[i]) + fuelLeft) - distances[i]

    minimum = min(fuelLeftList)
    return fuelLeftList.index(minimum)