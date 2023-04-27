def is_dna(seq):
    return True if 'U' not in seq else False


dna_seq = 'ACCCTTAGGAGCTACACT'
rna_seq = dna_seq.replace('T', 'U')
print(rna_seq)
print(dna_seq.count('C'))
print(is_dna(dna_seq))
print(is_dna(rna_seq))