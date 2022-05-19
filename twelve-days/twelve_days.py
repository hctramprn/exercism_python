def recite(start_verse, end_verse):
    song_dict = {1: ('first', 'a Partridge in a Pear Tree'), 2: ('second', 'two Turtle Doves'), 3: ('third', 'three French Hens'), 4: ('fourth', 'four Calling Birds'), 5: ('fifth', 'five Gold Rings'), 6: ('sixth', 'six Geese-a-Laying'), 7: (
        'seventh', 'seven Swans-a-Swimming'), 8: ('eighth', 'eight Maids-a-Milking'), 9: ('ninth', 'nine Ladies Dancing'), 10: ('tenth', 'ten Lords-a-Leaping'), 11: ('eleventh', 'eleven Pipers Piping'), 12: ('twelfth', 'twelve Drummers Drumming')}

    song_list = []
    song = ''
    for day in range(start_verse, end_verse + 1):
        song += f'On the {song_dict.get(day)[0]} day of Christmas my true love gave to me: '
        gifts = ''
        for gift in range(day, 0, -1):
            if gift > 1:
                gifts += f'{song_dict.get(gift)[1]}, '
            else:
                if day == start_verse == 1:
                    gifts += f'{song_dict.get(gift)[1]}.'
                else:
                    gifts += f'and {song_dict.get(gift)[1]}.'
        song += gifts
        song_list.append(song)
        song = ''
    return song_list
