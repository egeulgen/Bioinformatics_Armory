import sys
from Bio import SeqIO
from os import remove

if __name__ == "__main__":
    '''
    Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.
    Return: Number of reads in filtered FASTQ entries
    '''
    input_lines = sys.stdin.read().splitlines()
    threshold, percentage = map(int, input_lines[0].split())

    f = open("tmp.fastq", "w+")
    for line in input_lines[1:]:
        f.write(line + "\r\n")
    f.close()

    count = 0
    for record in SeqIO.parse("tmp.fastq", "fastq"):
        qual_list = record.letter_annotations["phred_quality"]
        tot_pass = sum(q >= threshold for q in qual_list)
        if tot_pass / len(qual_list) * 100 >= percentage:
            count += 1
    print(count)

    remove("tmp.fastq")