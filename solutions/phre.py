import sys
from Bio import SeqIO


if __name__ == "__main__":
    '''
    Given: A quality threshold, along with FASTQ entries for multiple reads.
    Return: The number of reads whose average quality is below the threshold.
    '''
    input_lines = sys.stdin.read().splitlines()
    threshold = int(input_lines[0])
    f = open("tmp.fastq", "w+")
    for line in input_lines[1:]:
        f.write(line + "\r\n")
    f.close()

    count = 0
    for record in SeqIO.parse("tmp.fastq", "fastq"):
        qual_list = record.letter_annotations["phred_quality"]
        if sum(qual_list) / len(qual_list) < threshold:
            count += 1

    print(count)