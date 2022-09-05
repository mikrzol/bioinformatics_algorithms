from random import randint
from tqdm import tqdm
from chapter_2.generate_profile import generate_profile
from chapter_2.profile_most_prob_kmer_2c import profile_most_probable_kmer
from chapter_2.greedy_motif_search_2d import generate_consensus
from chapter_1.hamming_distance_1g import hamming_distance


def score_motifs(motifs: list[str]) -> int:
    consensus = generate_consensus(generate_profile(motifs, laplace_succession=True))
    return sum([hamming_distance(consensus, motif) for motif in motifs])


def generate_motifs(profile_matrix: list[list[float]], dna_seqs: list[str], k: int) -> list[str]:
    return [profile_most_probable_kmer(seq, k, profile_matrix_list=profile_matrix) for seq in dna_seqs]


def randomized_motif_search(dna_seqs: list[str], k: int, t: int) -> list[str]:
    curr_motifs = []
    for seq in dna_seqs:
        start_idx = randint(0, len(seq) - k)
        curr_motifs.append(seq[start_idx:start_idx+k])

    best_motifs = curr_motifs

    while True:
        profile_mat = generate_profile(curr_motifs, laplace_succession=True)
        curr_motifs = generate_motifs(profile_mat, dna_seqs, k)

        if score_motifs(curr_motifs) < score_motifs(best_motifs):
            best_motifs = curr_motifs
        else:
            return best_motifs


def random_motif_search_wrapper(dna_seqs: list[str], k: int, t: int) -> list[str]:
    best_motifs = [seq[:k] for seq in dna_seqs]

    for i in tqdm(range(1000)):
        curr_motifs = randomized_motif_search(dna_seqs, k, t)
        if score_motifs(curr_motifs) < score_motifs(best_motifs):
            best_motifs = curr_motifs
        
    return best_motifs


if __name__ == '__main__':
    with open('chapter_2/inputs/randomized_motif_search.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k, t = map(int, text[0].strip().split(' '))
        dna_seqs = text[1:]
        print('\n'.join(random_motif_search_wrapper(dna_seqs, k, t)))