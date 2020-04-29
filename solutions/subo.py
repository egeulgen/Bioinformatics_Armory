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


def hamming_dist(string1, string2):
    ''' Calculate Hamming Distance between strings
    :param string1: string 1 (string)
    :param string2: string 2 (string)
    :return: the hamming distance bw/ string1 and string2 (integer)
    '''
    return sum([x != y for x, y in zip(string1, string2)])


def count_hamming(pattern, seq, dist=3):
    """Count number of matches within dist mismatches."""
    count = 0
    pat_len = len(pattern)
    for i in range(len(seq) - pat_len + 1):
        if hamming_dist(seq[i:i + pat_len], pattern) <= dist:
            count += 1
    return count


if __name__ == "__main__":
    if __name__ == "__main__":
        '''
        Given: Two DNA strings s and t in FASTA format that share some short inexact repeat r of 32-40 bp. 
        By "inexact" we mean that r may appear with slight modifications (each repeat differ by ≤3 changes/indels).
        Return: The total number of occurrences of r as a substring of s, followed by the total number of occurrences 
        of r as a substring of t.
        '''
        input_lines = sys.stdin.read().splitlines()
        dna_dict = parse_fasta(input_lines)
        s = list(dna_dict.values())[0]
        t = list(dna_dict.values())[1]

        pattern = "AAGGTCTGAGGCTGCATCCGATTCAGAGTCA"
        print(len(pattern))
        print(count_hamming(pattern, s), count_hamming(pattern,t))

