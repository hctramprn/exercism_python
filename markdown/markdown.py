import re

mkdwn_dict = {'###### ': ('<h6>', '</h6>'), '##### ': ('<h5>', '</h5>'), '#### ': ('<h4>', '</h4>'), '### ': ('<h3>', '</h3>'), '## ': (
    '<h2>', '</h2>'), '# ': ('<h1>', '</h1>'), 'lst': ('<li>', '</li>'), 'bold': ('<strong>', '</strong>'), 'italic': ('<em>', '</em>'), 'par': ('<p>', '</p>')}


def parse(markdown):
    # splits the string
    lines = markdown.split('\n')
    # declares the string that will have the html code
    res = ''
    # bool variable indicating if an opening unordered list tag is present
    list_present = False
    # loop that checks each splitted line
    for i in lines:
        # a <p> tag will be added if not turned off
        paragraph_needed = True
        # checks if a header is present and prepares the html code
        header_match = re.match('#{1,6} ', i)
        if header_match:
            header = re.match('#{1,6} ', i).group(0)
            i = mkdwn_dict[header][0] + i[len(header):] + mkdwn_dict[header][1]
            # a <p> tag is not already needed
            paragraph_needed = False

        # checks if there's a list and prepares the html code
        list_match = re.match(r'\* (.*)', i)
        if list_match:
            # if it's the first list item, adds a <ul> tag at the beginning
            if not list_present:
                i = '<ul>' + mkdwn_dict['lst'][0] + \
                    list_match.group(1) + mkdwn_dict['lst'][1]
                list_present = True
            else:
                # else, removes the closing </ul> tag from the previous loop step
                res = res[:-5]
                i = mkdwn_dict['lst'][0] + \
                    list_match.group(1) + mkdwn_dict['lst'][1]
            # closes the unordered list in case this is the last item
            i += '</ul>'
            # a <p> tag is not already needed
            paragraph_needed = False

        # checks if there's bold text
        bold_match = re.match('.*(__([ a-zA-Z]*)__).*', i)
        if bold_match:
            # substitutes the bold formated text with the strong tags
            i = re.sub(bold_match.group(
                1), mkdwn_dict['bold'][0] + bold_match.group(2) + mkdwn_dict['bold'][1], i)

        # checks if there's italic text
        italic_match = re.match('.*(_([ a-zA-Z]*)_).*', i)
        if italic_match:
            # substitutes the italic formated text with the em tags
            i = re.sub(italic_match.group(
                1), mkdwn_dict['italic'][0] + italic_match.group(2) + mkdwn_dict['italic'][1], i)

        # wrapps the content in a <p> tag if it wasn't turned off
        if paragraph_needed:
            i = mkdwn_dict['par'][0] + i + mkdwn_dict['par'][1]

        # adds the formated line to the res string
        res += i
    # returns the formated string
    return res
