def jumpingOnClouds(c):
    # every index of the array
    i = 0
    # number of steps
    steps = 0

    # using while loop to manipulate the iteration
    while i < len(c) - 1:
        if c[i] == 0:
            i = i + 2
            steps = steps + 1
        else:
            i = i - 1 + 2
            steps += 1
    return steps


print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))
