def recite(start, take=1):
    """Function that recites a given verse of the 99 Bottles of Beer song.
    :param start: int - Number of the verse in which the song will start
    :param take: int - Number of bottles that will be taken to finish the song

    This functions determines the lyric of each verse of the song '99 Bottles of Beer song' given a specific start and bottles taken.
    """

    # defines the list that will contain the verses
    song_lst = []
    # loops the verses constructing the lyric for each number of bottle
    for bottle in range(start, start - take, -1):
        if bottle == 2:
            lyric_1 = f'{bottle} bottles of beer on the wall, {bottle} bottles of beer.'
            lyric_2 = f'Take one down and pass it around, {bottle - 1} bottle of beer on the wall.'
        elif bottle == 1:
            lyric_1 = f'{bottle} bottle of beer on the wall, {bottle} bottle of beer.'
            lyric_2 = f'Take it down and pass it around, no more bottles of beer on the wall.'
        elif bottle == 0:
            lyric_1 = 'No more bottles of beer on the wall, no more bottles of beer.'
            lyric_2 = 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        else:
            lyric_1 = f'{bottle} bottles of beer on the wall, {bottle} bottles of beer.'
            lyric_2 = f'Take one down and pass it around, {bottle - 1} bottles of beer on the wall.'
        # appends the verse in a list format
        song_lst.append([lyric_1, lyric_2])

    # loop that adds an empty list for padding
    song = []
    for el in song_lst:
        song += el + ['']
    song.pop(-1)

    # returns the song
    return song
