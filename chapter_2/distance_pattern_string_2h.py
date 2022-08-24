from cmath import inf

from hamming_distance_1g import hamming_distance

def distance_between_pattern_and_string(pattern: str, dna_seqs: list[str]) -> int:
    k = len(pattern)
    distance = 0

    for seq in dna_seqs:
        hamming_dist = inf
        for i in range(0, len(seq) - k + 1):
            curr_kmer = seq[i:i+k]
            if hamming_dist > hamming_distance(pattern, curr_kmer):
                hamming_dist = hamming_distance(pattern, curr_kmer)
        distance += hamming_dist
    
    return distance


if __name__ == '__main__':
    with open('chapter_2/inputs/distance_pattern_string.txt', 'r') as in_fh:
        pattern, stuff = in_fh.read().strip().split('\n')
        dna_seqs = stuff.strip().split(' ')
        print(distance_between_pattern_and_string(pattern, dna_seqs))