import re

CONDONS = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine',
           'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan'}


def proteins(strand):
    """Function that returns the protein associated with the condons in a certain strand.

    :param strand: str - String of the given strand.
    return: list - List of the proteins in the strand.

    This function returns the protein associated with the condons present in a given strand.
    """

    lst = []
    condons_list = re.findall(r'\w{3}', strand)
    for condon in condons_list:
        if condon not in CONDONS.keys():
            break
        lst.append(CONDONS[condon])
    return lst
