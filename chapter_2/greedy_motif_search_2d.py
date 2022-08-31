from chapter_2.generate_profile import generate_profile
from chapter_2.profile_most_prob_kmer_2c import profile_most_probable_kmer
from chapter_1.hamming_distance_1g import hamming_distance
from tqdm import tqdm

def generate_consensus(profile_matrix: list[list[float]]) -> str:
    consensus = ''
    indices_helper = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }

    for i in range(len(profile_matrix[0])):
        col = [val[i] for val in profile_matrix]
        consensus += indices_helper[col.index(max(col))]
    
    return consensus


def score_motifs(motifs: list[str]) -> int:
    consensus = generate_consensus(generate_profile(motifs))
    return sum([hamming_distance(consensus, motif) for motif in motifs])


def greedy_motif_search(dna_seqs: list[str], k: int, t: int):
    best_motifs = [seq[:k] for seq in dna_seqs]

    for kmer in tqdm([dna_seqs[0][i:i+k] for i in range(len(dna_seqs[0]) - k + 1)]):
        new_motifs = [kmer]

        for i in range(1, t):
            new_motifs.append(profile_most_probable_kmer(dna_seqs[i], k, profile_matrix_list=generate_profile(new_motifs)))
        if score_motifs(new_motifs) < score_motifs(best_motifs):
            best_motifs = new_motifs
    
    return best_motifs


if __name__ == '__main__':
    with open('chapter_2/inputs/greedy_motif_search.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k, t = map(int, text[0].strip().split(' '))
        dna_seqs = text[1:]
        print(' '.join(greedy_motif_search(dna_seqs, k, t)))