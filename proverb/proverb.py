def proverb(*input_data, qualifier=None):
    # declares the list that will have the proverb's sentences
    prov = []
    # loops the given input_data and constructs each sentence
    for i in range(len(input_data) - 1):
        sentence = f'For want of a {input_data[i]} the {input_data[i + 1]} was lost.'
        prov.append(sentence)
    # if a qualifier is passed, adds it before the first word passed
    if qualifier:
        qual = f'{qualifier} {input_data[0]}'
    # else, test if the input list is empty and returns an empty list
    else:
        try:
            qual = input_data[0]
        except IndexError:
            return []
    # appends the final sentence
    final = f'And all for the want of a {qual}.'
    prov.append(final)
    # returns the list with the proverb's sentences
    return prov
