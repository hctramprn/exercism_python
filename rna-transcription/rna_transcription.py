transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna_strand):
    dna = ''
    for char in dna_strand:
        if char in transcription.keys():
            dna += transcription[char]
        else:
            dna += char
    return dna
