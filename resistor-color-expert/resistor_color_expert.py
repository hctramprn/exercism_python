bands = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9'
}

tolerances = {
    'grey': '0.05%',
    'violet': '0.1%',
    'blue': '0.25%',
    'green': '0.5%',
    'brown': '1%',
    'red': '2%',
    'gold': '5%',
    'silver': '10%'
}


def resistor_label(colors):
    if len(colors) > 1:
        *values, multiplier, tolerance = colors
        values_lst = [bands[val] for val in values]
        num = int(''.join(values_lst)) * (10**int(bands[multiplier]))

        if num < 1000:
            scale = 'ohms'
        elif num < 1000000:
            num = num / 1000
            scale = 'kiloohms'
        else:
            num = num / 1000000
            scale = 'megaohms'

        if num % 1 == 0:
            num = int(num)

        return f'{num} {scale} ±{tolerances[tolerance]}'

    else:
        return f'{bands[colors[0]]} ohms'
