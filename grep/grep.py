import re

FILE_TEXT = {
    "iliad.txt": """Achilles sing, O Goddess! Peleus' son;
His wrath pernicious, who ten thousand woes
Caused to Achaia's host, sent many a soul
Illustrious into Ades premature,
And Heroes gave (so stood the will of Jove)
To dogs and to all ravening fowls a prey,
When fierce dispute had separated once
The noble Chief Achilles from the son
Of Atreus, Agamemnon, King of men.\n""",
    "midsummer-night.txt": """I do entreat your grace to pardon me.
I know not by what power I am made bold,
Nor how it may concern my modesty,
In such a presence here to plead my thoughts;
But I beseech your grace that I may know
The worst that may befall me in this case,
If I refuse to wed Demetrius.\n""",
    "paradise-lost.txt": """Of Mans First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal tast
Brought Death into the World, and all our woe,
With loss of Eden, till one greater Man
Restore us, and regain the blissful Seat,
Sing Heav'nly Muse, that on the secret top
Of Oreb, or of Sinai, didst inspire
That Shepherd, who first taught the chosen Seed\n""",
}


def grep(pattern, flags, files):
    # declares the array that will hold the matches
    matches = []
    regex_pattern = pattern

    # if there's no x flag, search the whole sentence
    if 'x' not in set(flags):
        regex_pattern = f'.*{regex_pattern}.*'
    # inverts the matching pattern to avoid those that contain the given pattern
    if 'v' in set(flags):
        regex_pattern = f'(^((?!{regex_pattern}).)*$)'

    # changes the pattern for case sensitive flag
    if 'i' in set(flags):
        re_pattern = re.compile(regex_pattern, flags=re.IGNORECASE)
    else:
        re_pattern = re.compile(regex_pattern, flags=re.MULTILINE)

    # creates a list with all the file's sentences for matching x flag
    text_splitted_all = [
        sentence for file in files for sentence in FILE_TEXT[file].split('\n')]

    # loop of regex that creates a list of the pattern's ocurrences
    for file in files:
        # gets and splits the text of the file from the dict
        text = FILE_TEXT[file]
        text_splitted = text.split('\n')
        text_splitted_lower = [t.lower() for t in text_splitted]

        # creates the list with all the matches for inclusive or exclusive pattern
        if 'v' in set(flags):
            re_temp = re_pattern.findall(text)
            re_list = [text[0] for text in re_temp if len(text[0]) > 1]
        else:
            re_list = re_pattern.findall(text)

        # if l is passed as a flag, appends the file's name
        if 'l' in set(flags):
            if re_list:
                string = f'{file}\n'
                matches.append(string)
        # else iterates the list returning each finding
        else:
            for match in re_list:
                # prepares the default match format
                string = f'{match}\n'

                if 'x' in set(flags):
                    # continues the loop if the pattern in lowercase
                    # is not present as a whole sentence
                    if 'i' in set(flags):
                        if pattern.lower() not in text_splitted_lower:
                            string = ''
                            continue
                    # continues the loop if the pattern is not present
                    # as a whole sentence
                    else:
                        if pattern not in text_splitted_all:
                            string = ''
                            continue

                # adds the index of the match for n flag
                if 'n' in set(flags):
                    index = text_splitted.index(match) + 1
                    string = f'{index}:{string}'

                # add the file's name to the beginning of the
                # match in case more than 1 file is passed
                if len(files) > 1:
                    string = f'{file}:{string}'

                # appends the string to the matches list
                matches.append(string)
    # returns a joined string of all the matches
    return ''.join(matches)
