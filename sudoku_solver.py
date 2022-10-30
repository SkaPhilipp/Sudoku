import xlrd


# read excel input
input_file = ("sudoku_input.xls")
workbook = xlrd.open_workbook(input_file)
worksheet = workbook.sheet_by_index(0)

# initialise
rows = [[] for _ in range(9)]
columns = [[] for _ in range(9)]
quadrants = [[] for _ in range(9)]

# convert row and column number into quadrant
def quad(row, column):
    return 3*(row//3) + column//3


# store input
for row in range(9):
    #current_row = []
    for column in range(9):
        value = worksheet.cell_value(row,column)
        if value == "":
            rows[row].append("x")
            columns[column].append("x")
            quadrants[3*(row//3) + column//3].append("x")
        else:
            rows[row].append(str(int(value)))
            columns[column].append(str(int(value)))
            quadrants[quad(row,column)].append(str(int(value)))

# print the board
def print_board():
    for row in range(9):
        for column in range(9):
            print(rows[row][column], end = " ")
        print()


# check if value is allowed in cell
def is_valid(row, column, digit):
    digit = str(digit)
    return not((digit in rows[row]) or (digit in columns[column]) or (digit in quadrants[quad(row,column)]))


# get possible values for cell
def get_possible_values(row, column):
    possible_values = []
    for i in range(1,10):
        if is_valid(row,column,i):
            possible_values.append(i)
    return possible_values

# check sudoku for certain values
def fill_certain_values():
    for row in range(9):
        for column in range(9):
            if rows[row][column] == "x":
                values = get_possible_values(row,column)
                if len(values) == 1:
                    value = str(values[0])
                    columns[column][row] = value
                    rows[row][column] = value
                    quadrants[quad(row,column)][3*(row%3)+(column%3)] = value

                    # Show progress
                    print(f"Filled cell ({row+1},{column+1})")
                    print()


# set value in cell for possible moves
def set_value(row, column, value):
    value = str(value)
    columns[column][row] = value
    rows[row][column] = value
    quadrants[quad(row,column)][3*(row%3)+(column%3)] = value




# main function
def main():

    # print initial sudoku
    print_board()
    print()

    # test move
    #set_value(0,4,5)

    # solve sudoku
    runs = 5
    for _ in range(runs):
        fill_certain_values()
        print_board()
        print()

# run main
main()