import argparse

def parse_args():
    """Parse command line arguments

    Parse the command line arguments using argparse

    :return args: Arguments passed in from the command line
    """
    parser = argparse.ArgumentParser(description="Advent of Code Day 1")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to the input file")
    return parser.parse_args()

def readFile(inputPath):
    """Read the file and split columns into two lists

    Read in the file and parse the data line by line
    splitting the line by a space and converting the values to integers
    and appending them to listA and listB

    :param inputPath: Path to the input file
    :return listA: List of integers from the first column
    :return listB: List of integers from the second column
    """
    listA = []
    listB = []
    with open(inputPath) as inputFile:
        for line in inputFile:
            splitLine = line.split()
            try:
                listA.append(int(splitLine[0]))
                listB.append(int(splitLine[1]))
            except:
                print("Error: Could not convert to int or out of range")
        return listA, listB

def buildCountMap(list):
    """Build a count map of the list

    Build a count map of the list by iterating through the list
    and counting the number of times each element appears

    :param list: List of integers
    :return countMap: Dictionary containing the count of each element
    """
    countMap = {}
    for element in list:
        if element in countMap:
            countMap[element] += 1
        else:
            countMap[element] = 1
    return countMap

def findSum(list, map):
    """Find the sum of elements multiplied by their count

    Find the sum of the elements in the list multiplied by their count
    by iterating through the list and multiplying the element by its count
    in the map

    :param list: List of integers
    :param map: Dictionary containing the count of each element
    :return sum: Sum of the elements multiplied by their count
    """
    sum = 0
    for element in list:
        if element in map:
            sum += element * map[element]
    return sum

def main():
    # Process command line arguments
    args = parse_args()

    # Read in input.txt
    listA, listB = readFile(args.input)

    # Sort the lists in ascending order
    listA.sort()
    listB.sort()

    # Find the total distance between the two lists
    totalDistance = 0

    # Loop through the lists and find the absolute difference between the two values
    for i in range(len(listA)):
        totalDistance += abs(listA[i] - listB[i])
    print(f"Total distance between the two lists: {totalDistance}")

    countMap = buildCountMap(listB)
    sum = findSum(listA, countMap)

    print(f"Sum of the elements in list A multiplied by their count in list B: {sum}")

if __name__ == "__main__":
    # Main entry point
    main()