def CatandMouse(x, y, z):
    distanceA = abs(x - z)
    distanceB = abs(y - z)

    if distanceB == distanceA:
        return "Mouse C"
    elif distanceA < distanceB:
        return "Cat A"
    elif distanceB < distanceA:
        return "Cat B"
