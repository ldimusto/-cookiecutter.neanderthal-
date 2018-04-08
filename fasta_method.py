#!/usr/bin/python3
import io

class DNARecord(object):
    
    def __init__ (self,sequence, gene, species_name):
        self.sequence = sequence
        self.gene = gene
        self.species_name = species_name 

    def complement(self):
        replacement1 = self.sequence.replace('A','t')
        replacement2 = replacement1.replace('T', 'a')
        replacement3 = replacement2.replace('C','g')
        replacement4 = replacement3.replace('G','C')
        return replacement4.upper()

    
    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count+ t_count)/ length
        return at_content

    

    def set_variables(self, new_seq, new_gene_name, new_species_name):
        self.sequence = new_seq
        self.gene = new_gene_name
        self.species_name = new_species_name 


    def get_fasta(self):
        safe_species_name = self.species_name.replace(' ','_')
        header = '>' + self.gene + '_' + safe_species_name 
        return header + '\n' + self.sequence + '\n'


output = open("high_at.fasta", "w")

for d in my_dna_records:
    if d.get_AT() > 0.6:
        output.write(d.get_fasta())
        
d1 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapeins')
print(d1.get_fasta())

d2 = DNARecord('CGGCGGCGCGGCGCGGCG', 'ATP6', 'Gorilla gorilla')


for r in [d1, d2]:
    print(r.gene + r.species_name)
    print('AT is ' + str(r.get_AT()))
    print('complement is ' + r.complement())
    print(d1.complement())
    print(d2.complement())
   # print('The protein is ' + protein)
