import sys
from Bio import SeqIO
from os import remove

if __name__ == "__main__":
    '''
    Given: quality threshold q and FASTQ file 
    Return: Number of positions where mean base quality falls below given threshold
    '''
    input_lines = sys.stdin.read().splitlines()
    threshold = int(input_lines[0])

    f = open("tmp.fastq", "w+")
    for line in input_lines[1:]:
        f.write(line + "\r\n")
    f.close()

    positions = [0 for _ in range(len(input_lines[2]))]

    num_records = 0
    for record in SeqIO.parse("tmp.fastq", "fastq"):
        num_records += 1
        qual_list = record.letter_annotations["phred_quality"]
        positions = [sum(x) for x in zip(positions, qual_list)]

    count = sum(tot_q / num_records < threshold for tot_q in positions)
    print(count)

    remove("tmp.fastq")