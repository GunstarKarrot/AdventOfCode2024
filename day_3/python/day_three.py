import argparse

def parse_args():
    """Parse command line arguments

    Parse the command line arguments using argparse

    :return args: Arguments passed in from the command line
    """
    parser = argparse.ArgumentParser(description="Advent of Code Day 1")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to the input file")
    return parser.parse_args()

def read_input(input_file):
    tokenList = []
    with open(input_file) as file:
        for line in file:
            splitLine = line.split("mul(")
            for i in range(len(splitLine)):
                deeperSplit = splitLine[i].split(")")
                for j in range(len(deeperSplit)):
                    evenDeeperSplit = deeperSplit[j].split(",")
                    if len(evenDeeperSplit) > 1 and evenDeeperSplit[0].isdigit() and evenDeeperSplit[1].isdigit():
                        tokenList.append(evenDeeperSplit)
    return tokenList

def main():
    args = parse_args()
    tokenList = read_input(args.input)
    print(tokenList)
    sum = 0
    for token in tokenList:
        sum += int(token[0]) * int(token[1])

    print(sum)

if __name__ == "__main__":
    # Main entry point
    main()