import sys


def parse_fasta(lines):
    ''' Parse FASTA format
    :param lines: list of lines in FASTA format
    :return: dictionary of sequences
    '''
    sequences = {}
    tmp_seq = ""
    tmp_name = ""
    for line in lines:
        line = line.rstrip()
        if line.startswith(">"):
            if tmp_seq != "":
                sequences[tmp_name] = tmp_seq
                tmp_seq = ""
            tmp_name = line[1:]
        else:
            tmp_seq += line
    # final seq
    sequences[tmp_name] = tmp_seq
    return sequences


if __name__ == "__main__":
    '''
    Given: A collection of n (n≤10) DNA strings.
    Return: The number of given strings that match their reverse complements.
    '''
    input_lines = sys.stdin.read().splitlines()
    dna_seqs = parse_fasta(input_lines).values()

