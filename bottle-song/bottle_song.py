numbers = {0: 'no', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}


def recite(start, take=1):
    song = []
    for bottle_num in range(start, start - take, -1):
        if bottle_num == 2:
            b1 = 'bottles'
            b2 = 'bottle'
        elif bottle_num == 1:
            b1 = 'bottle'
            b2 = 'bottles'
        else:
            b1 = 'bottles'
            b2 = 'bottles'
        l1 = f'{numbers[bottle_num].capitalize()} green {b1} hanging on the wall,'
        l2 = l1
        l3 = 'And if one green bottle should accidentally fall,'
        l4 = f'There\'ll be {numbers[bottle_num - 1]} green {b2} hanging on the wall.'
        song.extend([l1, l2, l3, l4])
        if take > 1 and bottle_num - 1 is not (start - take):
            song.append('')
    return song
