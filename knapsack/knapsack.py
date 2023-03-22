# Import the combinations function from the itertools module
from itertools import combinations

# Define a function that takes in a maximum weight and a list of items
def maximum_value(maximum_weight, items):
    
    # Create an empty list to store all possible combinations of items
    candidates = []
    
    # Loop over all possible sizes of combinations
    for size in range(1, len(items)):
        
        # Generate all possible combinations of items of the current size
        all_combinations = tuple(combinations(items, size))
        
        # Add the current set of combinations to the candidates list
        candidates.extend(all_combinations)

    # Initialize a variable to keep track of the maximum value found so far
    value = 0
    
    # Loop over all possible combinations of items
    for comb in candidates:
        
        # Initialize variables to keep track of the total value and weight of the current combination
        temp_value = 0
        weight = 0
        
        # Loop over all items in the current combination
        for item in comb:
            
            # Check if adding the weight of the current item exceeds the maximum weight
            if (weight + item['weight']) <= maximum_weight:
                
                # If not, add the item's weight and value to the running totals
                weight += item['weight']
                temp_value += item['value']
                
            else:
                continue
        
        # Check if the total value of the current combination is greater than the current maximum value
        if temp_value > value:
            
            # If so, update the maximum value
            value = temp_value
    
    # Return the maximum value found
    return value
