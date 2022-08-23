from chapter_2.motif_enumeration_2a import motif_enumeration
from chapter_1.neighbors_1n import neighbors

if __name__ == '__main__':
    with open('chapter_2/inputs/motif_enumeration.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k, d = text[0].strip().split(' ')
        dna = text[1:]
        print(f'k = {k}, d = {d}')
        print(dna)
        print()
        print(motif_enumeration(dna, int(k), int(d)))