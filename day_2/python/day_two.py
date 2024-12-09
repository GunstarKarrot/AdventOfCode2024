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
    """Read the file parse the input into a list of lists of integers

    Read in the file and parse the data line by line
    splitting the line by a space and converting the values to integers
    and appending them to a list
    then appending that list to a meta list

    :param inputPath: Path to the input file
    :return list: List of lists of integers
    """
    metaList = []
    with open(inputPath) as inputFile:
        for line in inputFile:
            splitLine = line.split()
            intList = []
            try:
                for i in range(len(splitLine)):
                    intList.append(int(splitLine[i]))
                metaList.append(intList)
            except:
                print("Error: Could not convert to int or out of range")
        return metaList

def isContinuingTrend(isIncreasing, current, next):
    """Check if the trend is continuing

    Check if the trend is continuing by checking if the current int is
    less than the next int if the trend is increasing or greater than the
    next int if the trend is decreasing

    :param isIncreasing: Boolean value to determine if the trend is increasing or decreasing
    :param current: Current integer
    :param next: Next integer
    :return: True if the trend is continuing, False if the trend is not continuing
    """
    if isIncreasing:
        return current < next
    else:
        return current > next

def isWithinRange(current, next, min, max):
    """Check if the difference between the two ints is within the range

    Check if the difference between the two ints is within the range

    :param current: Current integer
    :param next: Next integer
    :param min: Minimum value for the range
    :param max: Maximum value for the range
    :return: True if the difference is within the range, False if the difference is not within the range
    """
    diff = abs(current - next)
    return min <= diff <= max

def listIsStrictlySafe(list):
    """Check if the order of the ints is safe or unsafe

    Check if the order of the ints is safe or unsafe according to the following safety rules:
    1. The order of the ints must be only increasing or decreasing
    2. Any two adjacent ints must differ by at least 1 and at most 3

    :param list: List of integers
    :return: True if the order is safe, False if the order is unsafe
    """
    # Check if the list is empty
    if len(list) > 1 and (list[0] == list[1]):
        return False

    # Check if the list is increasing or decreasing
    isIncreasing = list[0] < list[1]

    for i in range(1,len(list)):
        # First check if the list is STILL increasing or decreasing
        if not isContinuingTrend(isIncreasing, list[i-1], list[i]):
            return False

        # Now check if the difference between the two adjacent ints is between 1 and 3
        if not isWithinRange(list[i-1], list[i], 1, 3):
            return False

    return True # If all checks pass, return True

def main():
    """Main function

    Main function for the script
    First parse the command line arguments
    then pass the input file path to the readFile function
    then iterate through the list of lists.
    For each list of ints, check if the order of the ints is considered
    safe or unsafe according to the following safety rules:
    1. The order of the ints must be only increasing or decreasing
    2. Any two adjacent ints must differ by at least 1 and at most 3

    :return: None
    """
    args = parse_args()
    metaList = readFile(args.input)
    safeCount = 0
    safeList = []
    unsafeList = []
    for list in metaList:
        safe = listIsStrictlySafe(list)
        if safe:
            safeCount += 1
            safeList.append(list)
        else:
            unsafeList.append(list)
        #print(f"List: {list} is {safe}")
    print(f"Safe count: {safeCount}")

    print(f"Engage the Problem Dampener!")


    # Problem Dampener i.e. Part 2
    # I have split the safe and unsafe lists into two separate lists
    # I will iterate through the unsafe list and for each list, I will
    # iterate through each element and create a new list without that element
    # I will then check if the new list is safe or not
    # If the new list is safe, I will increment the dampenedSafeCount and break from the loop
    dampenedSafeCount = safeCount
    for list in unsafeList:
        for i in range(len(list)):
            tempList = list.copy()
            tempList.pop(i)
            safe = listIsStrictlySafe(tempList)
            if safe:
                dampenedSafeCount += 1
                break
        #print(f"Originally Unsafe List: {list} is {safe}, Dampened Safe Count: {dampenedSafeCount}")
    print(f"Safe count: {dampenedSafeCount}")

    print(f"Strict Safe Count: {safeCount} Dampened Safe Count: {dampenedSafeCount}")


if __name__ == "__main__":
    # Main entry point
    main()