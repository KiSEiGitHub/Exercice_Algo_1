for x in range(-10, 11):
    for y in range(-10, 11):
        for z in range(-10, 11):
            if x + y - 3 * z == -10 and x - y + 2* z == 3 and 2 * x + y - z == -6:
                print(x, y, z)