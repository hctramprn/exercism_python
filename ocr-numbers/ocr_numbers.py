numbers = (
    [" _ ", "| |", "|_|", "   "],
    ["   ", "  |", "  |", "   "],
    [" _ ", " _|", "|_ ", "   "],
    [" _ ", " _|", " _|", "   "],
    ["   ", "|_|", "  |", "   "],
    [" _ ", "|_ ", " _|", "   "],
    [" _ ", "|_ ", "|_|", "   "],
    [" _ ", "  |", "  |", "   "],
    [" _ ", "|_|", "|_|", "   "],
    [" _ ", "|_|", " _|", "   "]
)

def convert(input_grid):
    # checks if number of rows is a mutiple of four
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    # checks if the number of columns is a multiple three
    for line in input_grid:
        if len(line) % 3 != 0:
            raise ValueError(
                "Number of input columns is not a multiple of three")

    # defines the string of the ocr numbers
    ocr_num = ''
    # defines the row counter and loops while its
    # value is less than the length of the grid
    row = 0
    while row < len(input_grid):
        # defines the column counter and loops while its
        # value is less than the length of the first element
        column = 0
        while column < len(input_grid[0]):
            # creates chunks of possible numbers
            possible_char = []
            for i in range(row, row + 4):
                possible_char.append(input_grid[i][column:column + 3])
            # adds the increment of 3 columns
            column += 3

            # if the chunk is in the tuple of numbers, adds its index
            if possible_char in numbers:
                ocr_num += str(numbers.index(possible_char))
            # else, adds a ? sign
            else:
                ocr_num += '?'
        
        # adds the increment of 4 rows and if 
        # its not the final row, adds a comma
        row += 4
        if row < len(input_grid):
            ocr_num += ','
    return ocr_num