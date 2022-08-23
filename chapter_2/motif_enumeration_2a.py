from chapter_1.neighbors_1n import neighbors
from chapter_1.hamming_distance_1g import hamming_distance

def motif_enumeration(dna_seqs: list[str], k: int, d: int) -> set[str]:
    patterns = set()
    for i in range(0, len(dna[0]) - k + 1):
        pattern = dna_seqs[0][i:i+k]
        neighs = neighbors(pattern, d)

        for neighbor in neighs:
            count = 0
            for seq in dna_seqs:
                for j in range(0, len(seq) - k + 1):
                    curr_ptrn = seq[j:j+k]
                    if  hamming_distance(neighbor, curr_ptrn) <= d:
                        count += 1
                        break
            if count == len(dna_seqs):
                patterns.add(neighbor)

    return patterns


if __name__ == '__main__':
    with open('chapter_2/inputs/motif_enumeration.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k, d = text[0].strip().split(' ')
        dna = text[1:]
        with open('chapter_2/res.txt', 'w') as out_fh:
            out_fh.write(' '.join(sorted(list(motif_enumeration(dna, int(k), int(d))))))
