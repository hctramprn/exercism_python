resistor_values = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3',
                   'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}

def label(colors):
    res_val = ''
    for color in colors[:-1]:
        res_val += resistor_values[color]
    res_val += '0' * int(resistor_values[colors[-1]])

    if '000' in res_val:
        res_val = res_val[:-3] + ' kiloohms'
    else:
        res_val += ' ohms'
    return res_val
