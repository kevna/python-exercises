def read_data(filename):
    result = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            result.append(line)
    return result
