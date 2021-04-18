def readData(filename):
    result = []
    with open(filename) as file:
        for line in file:
            result.append(line)
    return result
