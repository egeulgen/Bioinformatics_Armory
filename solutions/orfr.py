import sys
from Bio.Seq import translate, reverse_complement


if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 10 kbp, and a protein string translated by s.
    Return: The index of the genetic code variant that was used for translation. 
    (If multiple solutions exist, you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    dna_seq = input_lines[0]
    rev_dna_seq = reverse_complement(dna_seq)

    max_len = 0
    best_pr = ""
    for i in range(len(dna_seq) - 2):
        for j in range(len(dna_seq) - 1, i + 1, -1):
            subseq = dna_seq[i:j]
            if subseq[:3] == "ATG":
                translated = translate(subseq, to_stop=True)
                if len(translated) > max_len:
                    max_len = len(translated)
                    best_pr = translated
    for i in range(len(rev_dna_seq) - 2):
        for j in range(len(rev_dna_seq) - 1, i + 1, -1):
            subseq = rev_dna_seq[i:j]
            if subseq[:3] == "ATG":
                translated = translate(subseq, to_stop=True)
                if len(translated) > max_len:
                    max_len = len(translated)
                    best_pr = translated
    print(best_pr)
