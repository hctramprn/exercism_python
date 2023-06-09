from itertools import permutations

def solve(puzzle):
    equation = []  # Stores the groups of characters in the equation
    temp_str = ''  # Temporary string to build each group

    # Iterate over each character in the puzzle
    for char in puzzle:
        if char.isalpha():
            temp_str += char  # Add the character to the temporary string
        else:
            if len(temp_str):
                equation.append(temp_str)  # Append the completed group to the equation list
                temp_str = ''  # Reset the temporary string
    equation.append(temp_str)  # Append the remaining group (if any) to the equation list

    characters = tuple(set([char for char in puzzle if char.isalnum()]))  # Get unique alphanumeric characters

    possible_dicts = combination_generator(characters, equation)  # Generate possible combinations of values

    # Iterate over each combination
    for comb in possible_dicts:
        first_characters = [comb[group[0]] for group in equation if len(group) > 1]

        # Check if 0 is not present in the first characters of groups
        if 0 not in first_characters:
            return comb  # Return the valid combination

def combination_generator(characters, equation):
    possible_values = permutations(range(10), len(characters))  # Generate all possible value permutations

    # Separate the equation into left and right parts
    left_lst, right_lst = equation[:-1], equation[-1:]

    # Iterate over each combination of values
    for comb in possible_values:
        temp_dict = dict(zip(characters, comb))  # Create a temporary dictionary with character-value mappings

        left_values = []
        # Construct the numerical values for the left part of the equation
        for group in left_lst:
            temp_val = ''
            for char in group:
                temp_val += str(temp_dict[char])
            left_values.append(int(temp_val))

        # Construct the numerical value for the right part of the equation
        right_value = int(''.join([str(temp_dict[char]) for char in right_lst[0]]))

        # Check if the equation holds true
        if sum(left_values) == right_value:
            yield temp_dict  # Yield the valid combination
