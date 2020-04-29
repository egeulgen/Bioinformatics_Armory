import sys
from Bio.Seq import translate


if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 10 kbp, and a protein string translated by s.
    Return: The index of the genetic code variant that was used for translation. 
    (If multiple solutions exist, you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    dna_seq = input_lines[0]
    protein_seq = input_lines[1]

    for i in [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33]:
        translated = translate(dna_seq, table=i, stop_symbol="", to_stop=False)
        if protein_seq == translated:
            print(i)
            break

