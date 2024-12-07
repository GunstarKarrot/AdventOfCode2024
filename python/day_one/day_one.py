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
    # distanceList = []

    # Calculate the distance between the two lists
    # for i in range(len(listA)):
    #     distanceList.append(abs(listA[i] - listB[i]))
    # print each list as columns
    # print("List A\tList B\tDistance")
    # for i in range(len(listA)):
    #     print(f"{listA[i]}\t{listB[i]}\t{distanceList[i]}")

    for i in range(len(listA)):
        totalDistance += abs(listA[i] - listB[i])
    print(f"Total distance between the two lists: {totalDistance}")

if __name__ == "__main__":
    # Main entry point
    main()