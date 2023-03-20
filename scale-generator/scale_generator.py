# list with the notes for each key signature
SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

# dict of the corresponding key signature for each note
note_dict = {'C': SHARPS, 'G': SHARPS, 'D': SHARPS, 'A': SHARPS, 'E': SHARPS, 'B': SHARPS, 'F#': SHARPS, 'a': SHARPS, 'e': SHARPS, 'b': SHARPS, 'f#': SHARPS, 'c#': SHARPS, 'g#': SHARPS, 'd#': SHARPS, 'F': FLATS, 'Bb': FLATS,  'Eb': FLATS, 'Ab': FLATS, 'Db': FLATS, 'Gb': FLATS, 'd': FLATS, 'g': FLATS, 'c': FLATS, 'f': FLATS, 'bb': FLATS, 'eb': FLATS,}

#class that determines if a given note uses sharps or flats
class Scale:
    # intis the class with the given tonic
    def __init__(self, tonic):
        self.tonic = tonic

    # returns the chromatic scale (12 notes) of the tonic
    def chromatic(self):
        notes = note_dict[self.tonic] * 2
        start_index = notes.index(self.tonic.capitalize())
        return notes[start_index:start_index + 12]

    # returns the notes that correspond to the scale chosen
    def interval(self, intervals):
        # inits an empty list and appends the step to the next note
        steps = []
        for key in intervals:
            if key == 'm':
                steps.append(1)
            elif key == 'M':
                steps.append(2)
            elif key == 'A':
                steps.append(3)
        # creates an empty list where the notes will be stored
        interval_lst = []

        # gets the notes accordingly to the steps of the interval passed
        notes_lst = self.chromatic() * 2
        counter = 0
        for i in range(len(intervals) + 1):
            interval_lst.append(notes_lst[counter])
            try:
                counter += steps[i]
            except:
                continue
        # returns the list with the notes of the scale
        return interval_lst
