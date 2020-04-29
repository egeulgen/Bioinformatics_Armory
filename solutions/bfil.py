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

    to_rm_dict = {}
    for i in range(1, len(input_lines) - 2, 4):
        idx = i // 4
        to_rm_dict[idx] = []

    for idx, record in enumerate(SeqIO.parse("tmp.fastq", "fastq")):
        qual_list = record.letter_annotations["phred_quality"]
        # leading
        for i in range(len(qual_list)):
            if qual_list[i] < threshold:
                to_rm_dict[idx].append(i)
            else:
                break
        # trailing
        for j in range(len(qual_list) - 1, -1, -1):
            if qual_list[j] < threshold:
                if idx in to_rm_dict:
                    to_rm_dict[idx].append(j)
                else:
                    to_rm_dict[idx] = [j]
            else:
                break

    for i in range(1, len(input_lines) - 2, 4):
        idx = i // 4

        print(input_lines[i])

        seq = input_lines[i + 1]
        seq = "".join([s for pos, s in enumerate(seq) if pos not in to_rm_dict[idx]])
        print(seq)

        print("+")

        qual = input_lines[i + 3]
        qual = "".join([q for pos, q in enumerate(qual) if pos not in to_rm_dict[idx]])
        print(qual)

    remove("tmp.fastq")