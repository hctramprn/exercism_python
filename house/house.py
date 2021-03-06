lyrics = {1: ' the house that Jack built', 2: ' the malt that lay in', 3: ' the rat that ate', 4: ' the cat that killed', 5: ' the dog that worried', 6: ' the cow with the crumpled horn that tossed', 7: ' the maiden all forlorn that milked',
          8: ' the man all tattered and torn that kissed', 9: ' the priest all shaven and shorn that married', 10: ' the rooster that crowed in the morn that woke', 11: ' the farmer sowing his corn that kept', 12: ' the horse and the hound and the horn that belonged to'}


def recite(start_verse, end_verse):
    """Function that returns an array of verses of the rhyme 'This is the House that Jack Built.

    :param start_verse: int - Marks the start of the verses in the array.
    :param end_verse: int - Marks the end of the verses in the array.
    :return: list - The verses of the rhyme given the start and end points.

    This function takes two points of the rhyme 'This is the House that Jack Built' and creats an array of strings of each verse.
    """

    # starts an empty array in which the verses will be stored
    rhyme = []
    # Loops through the lyric dict creating each verse.
    for verse in range(start_verse, end_verse + 1):
        song = ''
        for step in range(1, verse + 1):
            song = lyrics[step] + song
        song = 'This is' + song + '.'
        rhyme.append(song)
    return rhyme
