import io
imoort argparse

def parse_args():
    """Parse command line arguments

    Parse the command line arguments using argparse

    :return args: Arguments passed in from the command line
    """
    parser = argparse.ArgumentParser(description="Advent of Cod
e Day 1")                                                          parser.add_argument("-i", "--input", type=str, required=Tru
e, help="Path to the input file")                                  return parser.parse_args()

def read_file(file_path):
    """Read the input file

    Read the input file into a dictionary, followed by a list.
    The inputs will be a two column line list, seperated by the pipe character. After this section, there will be a multiple line comma seperated list.

    The two column section should be seperated into a dictionary, with the first column as the key and the second column as the value.

    The multiple line section should be seperated into a list, with each line as an element in the list.

    :param file_path: Path to the input file
    """
    with open(file_path, 'r') as file:
        for line in file:
            print(line)

def main():
    args = parse_args()
    read_file(args.input) 

if __name__ == '__main__':
    main()
