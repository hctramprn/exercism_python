def tally(rows):
    # splits the given rows into three columns
    results_split = [s.split(';') for s in rows]

    # updates the team's names
    teams = set()
    for t in results_split:
        teams.add(t[0])
        teams.add(t[1])

    # declares a list for each result and fills them
    w, l, d = [], [], []
    for res in results_split:
        if res[2] == 'draw':
            d.append(res[0])
            d.append(res[1])
        else:
            if res[2] == 'win':
                w.append(res[0])
                l.append(res[1])
            else:
                w.append(res[1])
                l.append(res[0])

    # creates the scoreboard's format and appends each row to the sb list
    sb = []
    for t in teams:
        won = w.count(t)
        lost = l.count(t)
        drawn = d.count(t)
        matches = won + lost + drawn
        points = (won * 3) + (drawn * 1)
        result_string = f'{t.ljust(31)}|  {str(matches)} |  {str(won)} |  {str(drawn)} |  {str(lost)} |{str(points).rjust(3)}'

        sb.append((points, result_string))

    # sorts the rows by score (ascending) and alphabetically (descending)
    sorted_scoreboard = sorted(sb, key=lambda x: (-x[0], x[1]))
    # extracts the string
    rows = [tup[1] for tup in sorted_scoreboard]

    # prepares the header and returns the scoreboard
    scoreboard = ['Team                           | MP |  W |  D |  L |  P']
    return scoreboard + rows
