import sys
from Bio.Seq import Seq


if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 1000 bp.
    Return: Four integers (separated by spaces) representing the respective number of times that the symbols 
    'A', 'C', 'G', and 'T' occur in s.
    '''
    DNA_seq = Seq(sys.stdin.read().splitlines()[0])

    result = []
    for n in "ACGT":
        result.append(str(DNA_seq.count(n)))

    print(" ".join(result))