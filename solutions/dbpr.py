import sys
from Bio import ExPASy
from Bio import SwissProt


if __name__ == "__main__":
    '''
    Given: The UniProt ID of a protein.
    Return: A list of biological processes in which the protein is involved (biological processes are found in a 
    subsection of the protein's "Gene Ontology" (GO) section).
    '''
    uniprot_id = sys.stdin.read().splitlines()[0]

    handle = ExPASy.get_sprot_raw(uniprot_id)
    record = SwissProt.read(handle)

    print(record.cross_references[0])
