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
    """Read input file as a 2d grid of chars

    Read the input file and turn it into a 2d array grid of characters

    :param input_file: Path to the input file
    :return grid: 2d grid of characters
    """
    grid = []
    with open(input_file) as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

def check_horizontal(grid, row, col):
    """Check for the word MAS horizontally

    Check for the word "XMAS" after receiving the index of "X".
    Check horizontally in the grid, both forwards and backwards.
    Check if there is enough space to check for the word in
    both directions. Then check if the word is present in both directions.

    :param grid: 2d grid of characters
    :param row: row index
    :param col: column index
    :return total: total number of "MAS" found
    """
    total = 0
    if not col + 3 >= len(grid[row]):
        if grid[row][col + 1] == "M" and grid[row][col + 2] == "A" and grid[row][col + 3] == "S":
            total += 1
    if not col - 3 < 0:
        if grid[row][col - 1] == "M" and grid[row][col - 2] == "A" and grid[row][col - 3] == "S":
            total += 1

    return total

def check_vertical(grid, row, col):
    """Check for the word MAS vertially

    Check for the word "XMAS" after receiving the index of "X".
    Check veritcally in the grid, both forwards and backwards.
    Check if there is enough space to check for the word in
    both directions. Then check if the word is present in both directions.

    :param grid: 2d grid of characters
    :param row: row index
    :param col: column index
    :return total: total number of "MAS" found
    """
    total = 0
    if not row + 3 >= len(grid):
        if grid[row + 1][col] == "M" and grid[row + 2][col] == "A" and grid[row + 3][col] == "S":
            total += 1
    if not row - 3 < 0:
        if grid[row - 1][col] == "M" and grid[row - 2][col] == "A" and grid[row - 3][col] == "S":
            total += 1

    return total

def check_diagonal(grid, row, col):
    """Check for the word MAS horizontally

    Check for the word "XMAS" after receiving the index of "X".
    Check horizontally in the grid, both forwards and backwards.
    Check if there is enough space to check for the word in
    both directions. Then check if the word is present in both directions.

    :param grid: 2d grid of characters
    :param row: row index
    :param col: column index
    :return total: total number of "MAS" found
    """
    total = 0
    if not row + 3 >= len(grid) and not col + 3 >= len(grid[row]):
        if grid[row + 1][col + 1] == "M" and grid[row + 2][col + 2] == "A" and grid[row + 3][col + 3] == "S":
            total += 1
    if not row - 3 < 0 and not col - 3 < 0:
        if grid[row - 1][col - 1] == "M" and grid[row - 2][col - 2] == "A" and grid[row - 3][col - 3] == "S":
            total += 1
    if not row + 3 >= len(grid) and not col - 3 < 0:
        if grid[row + 1][col - 1] == "M" and grid[row + 2][col - 2] == "A" and grid[row + 3][col - 3] == "S":
            total += 1
    if not row - 3 < 0 and not col + 3 >= len(grid[row]):
        if grid[row - 1][col + 1] == "M" and grid[row - 2][col + 2] == "A" and grid[row - 3][col + 3] == "S":
            total += 1

    return total

def main():
    input = parse_args()
    grid = read_input(input.input)

    totalFinds = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                h = check_horizontal(grid, i, j)
                v = check_vertical(grid, i, j)
                d = check_diagonal(grid, i, j)
                totalFinds += h + v + d

    print(totalFinds)


if __name__ == "__main__":
    main()