import io

class DNARecord():
    
    def __init__ (self):
        self.sequence = 'sequence' 
        self.gene = 'gene' 
        self.species_name = 'species_name' 

    def get_AT(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        at_content = (a_count+ t_count)/ length
        return at_content

    def complement(self):
        replacement1 = self.sequence.replace('A','t')
        replacement2 = replacement1.replace('T', 'a')
        replacement3 = replacement2.replace('C','g')
        replacement4 = replacement3.replace('G','C')
        return replacement4.upper()

d1 = DNARecord()
d1.sequence = 'ATATATTATTATATTATA'
d1.gene = 'COX1'
d1.species_name = 'Homo sapiens'

d2 = DNARecord()
d2.sequence = 'CGGCGGCGCGGCGCGGCG'
d2.gene = 'ATP6'
d2.species_name = 'Gorilla gorilla'

for r in [d1, d2]:
    print('Created a record for ' + r.gene + ' from ' + r.species_name)
    print('AT is ' + str(r.get_AT()))
    print('complement is ' + r.complement())