operators = {'plus': '+', 'minus': '-', 'multiplied': '*', 'divided': '/'}


def answer(question):
    """Function that evaluates simple math problems and returns the answer.

    :param question: str - string containing the question.
    :return: int - the math problem evaluated.

    This function evaluates the math problem in a question an returns the answer in case there are not complex operators or the syntax is not clear.

    """

    question_list = question.replace('What is', '').replace(
        '?', '').replace('by', '').split()
    expression_list = []
    if not len(question_list):
        raise ValueError("syntax error")

    for element in question_list:
        if element in operators.keys():
            expression_list.append(operators[element])
        else:
            try:
                expression_list.append(str(int(element)))
            except:
                raise ValueError("unknown operation")

    expression_eval = ''
    result = 0
    for step in range(0, len(expression_list), 3):
        try:
            expression_eval = ' '.join(expression_list[0:3])
            result = eval(expression_eval)
            expression_list = expression_list[3:]
            expression_list.insert(0, str(result))
        except:
            raise ValueError("syntax error")

    return result
