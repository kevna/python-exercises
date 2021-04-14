def readData(fileName):
    result = []
    with open(fileName) as fileHandle:
        for line in fileHandle:
            result.append(line)
    return result
