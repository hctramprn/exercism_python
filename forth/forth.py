class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    # define the default functions that can be used in the input
    def dup(stack):
        duplicate_lst = stack + stack[-1:]
        return duplicate_lst

    def drop(stack):
        drop_lst = stack[:-1]
        return drop_lst

    def swap(stack):
        if len(stack) < 2:
            raise StackUnderflowError('Insufficient number of items in stack')
        swap_lst = stack[:-2] + [stack[-1], stack[-2]]
        return swap_lst

    def over(stack):
        if len(stack) < 2:
            raise StackUnderflowError('Insufficient number of items in stack')
        over_lst = stack + [stack[-2]]
        return over_lst

    # create a dictionary to store the definitions of new words
    definition_dict = {'dup': dup, 'drop': drop, 'swap': swap, 'over': over}

    # if there are new definitions, update the definition_dict accordingly
    if len(input_data) > 1:
        for word_definition in input_data[:-1]:
            # parse the input line into a list of lowercase strings
            word_definition_lst = [char.lower()
                                   for char in word_definition[2:-2].split(' ')]
            # the first element of the list is the new word name, the rest is the new definition
            word_name, *new_def = word_definition_lst
            temp_definition = []
            # iterate over the new definition and update a temporary definition
            for definition in new_def:
                if definition in definition_dict.keys():
                    if definition not in ['dup', 'drop', 'swap', 'over']:
                        temp_definition.append(definition_dict[definition][0])
                    else:
                        temp_definition.append(definition)
                else:
                    temp_definition.append(definition)
            # update the definition_dict with the new word definition
            definition_dict.update({word_name: temp_definition})
    # if there is only one input line and it starts with a colon, raise a ValueError
    elif input_data[0][0] == ':':
        raise ValueError('illegal operation')

    # parse the input line into a list of lowercase strings
    input_lst = [element.lower() for element in input_data[-1].split(' ')]
    # apply the word definitions in the dictionary to the input until the maximum number of levels is reached
    levels = 0
    while levels < 3:
        temp_lst = []
        for element in input_lst:
            if element in definition_dict.keys():
                if callable(definition_dict[element]):
                    temp_lst.append(definition_dict[element])
                else:
                    temp_lst += definition_dict[element]
            else:
                temp_lst.append(element)
        input_lst = temp_lst
        levels += 1

    # initialize an empty stack_lst to store the values in the input
    stack_lst = []
    while input_lst:
        value = input_lst[0]
        try:
            # If the value can be converted to an integer, it is added to the stack
            stack_lst.append(int(value))
        except:
            # If the value is a function, it is executed on the stack
            if callable(value):
                # If the stack is empty, a StackUnderflowError is raised
                if not stack_lst:
                    raise StackUnderflowError(
                        'Insufficient number of items in stack')
                # If the value is a function that takes a stack as its argument, it is called
                # with the current stack as its argument and the new stack is assigned to
                # stack_lst.
                new_stack = value(stack_lst)
                stack_lst = new_stack

            # If the value is an arithmetic operator, it is applied to the top two items of the stack
            elif value in '+-*/':
                # If there are fewer than two items in the stack, a StackUnderflowError is raised
                if len(stack_lst) < 2:
                    raise StackUnderflowError(
                        'Insufficient number of items in stack')
                try:
                    # The arithmetic operation is evaluated using eval() and the result is
                    # added to the stack as an integer.
                    answer = eval(
                        str(stack_lst[-2]) + value + str(stack_lst[-1]))
                    stack_lst = [int(answer)]
                except ZeroDivisionError:
                    raise ZeroDivisionError('divide by zero')
            else:
                # If the value is not an integer, a function, or an arithmetic operator, a ValueError is raised.
                raise ValueError('undefined operation')

        # The processed value is removed from the input_lst.
        input_lst.pop(0)
    # The final state of the stack is returned.
    return stack_lst
