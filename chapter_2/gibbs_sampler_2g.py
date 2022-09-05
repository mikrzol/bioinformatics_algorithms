import numpy as np
from tqdm import tqdm
from random import randint
from chapter_2.generate_profile import generate_profile
from chapter_2.greedy_motif_search_2d import generate_consensus
from chapter_1.hamming_distance_1g import hamming_distance


def score_motifs(motifs: list[str]) -> int:
    consensus = generate_consensus(generate_profile(motifs, laplace_succession=True))
    return sum([hamming_distance(consensus, motif) for motif in motifs])


def kmer_probability(kmer: str, profile_dict: dict) -> float:
    return np.prod([profile_dict[nucl][i] for i, nucl in enumerate(kmer)])


def profile_randomly_gen_kmer(seq: str, k: int, profile: list[float]):
    profile_dict = dict(zip(['A', 'C', 'G', 'T'], profile))
    probabilities = [kmer_probability(kmer, profile_dict) for kmer in [seq[i:i+k] for i in range(len(seq) - k + 1)]]
    # 'normalize' the probabilities
    total = sum(probabilities)
    probabilities = [prob/total for prob in probabilities]
    chosen_idx = np.random.choice(len(seq) - k + 1, p = probabilities)

    return seq[chosen_idx:chosen_idx+k]


def gibbs_sampler(dna_seqs: list[str], k: int, t: int, N: int) -> list[str]:
    motifs = []
    for seq in dna_seqs:
        start_idx = randint(0, len(seq) - k)
        motifs.append(seq[start_idx:start_idx+k])
    
    best_motifs = motifs

    for j in range(N+1):
        i = randint(0, t-1)
        profile = generate_profile([motifs[idx] for idx in range(len(motifs)) if idx != i], laplace_succession=True)
        motifs[i] = profile_randomly_gen_kmer(dna_seqs[i], k, profile)

        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs
    
    return best_motifs


def gibbs_sampler_wrapper(dna_seqs: list[str], k: int, t: int, N: int) -> list[str]:
    best_motifs = gibbs_sampler(dna_seqs, k, t, N)

    for i in tqdm(range(20)):
        curr_motifs = gibbs_sampler(dna_seqs, k, t, N)
        if score_motifs(curr_motifs) < score_motifs(best_motifs):
            best_motifs = curr_motifs
        
    return best_motifs


if __name__ == '__main__':
    with open('chapter_2/inputs/gibbs_sampler.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k, t, N = map(int, text[0].strip().split(' '))
        dna_seqs = text[1:]
        print('\n'.join(gibbs_sampler_wrapper(dna_seqs, k, t, N)))