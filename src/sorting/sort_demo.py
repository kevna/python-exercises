"""This module unfinished as it's inherited from a university module
"""

def read_data(filename):
    """Read sampole data file to demonstrate sorting.
    """
    result = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            result.append(line)
    return result
