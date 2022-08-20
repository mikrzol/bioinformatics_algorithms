from pattern_to_number_1l import pattern_to_number
from number_to_pattern_1m import number_to_pattern
from neighbors_1n import neighbors
from reverse_complement_1c import reverse_complement
# import time
# from tqdm import tqdm

def computing_freqs_w_mismatches_rev_compl(text: str, k: int, d: int) -> set[str]:
    freq_arr = [[0] * (4**k), [0] * (4**k)]

    for i in range(0, len(text) - k + 1):
        neighborhood_normal = list(neighbors(text[i:i+k], d))
        neighborhood_rev_compl = list(neighbors(reverse_complement(text[i:i+k]), d))
        for x in range(0, len(neighborhood_normal)):
            j_normal = pattern_to_number(neighborhood_normal[x])
            freq_arr[0][j_normal] += 1
            
            j_rev_compl = pattern_to_number(neighborhood_rev_compl[x])
            freq_arr[1][j_rev_compl] += 1

    return freq_arr

def faster_frequent_words_with_mismatches(text: str, k: int, d: int) -> set[str]:
    '''
    text:   sequence to find frequent words in
    k:      length of k-mer
    d:      number of allowed mismatches (Hamming distance)
    '''
    frequent_patterns = set()
    freq_arr_normal, freq_arr_rev_compl = computing_freqs_w_mismatches_rev_compl(text, k, d)

    freq_arr_summed = [a + b for a, b in zip(freq_arr_normal, freq_arr_rev_compl)]
    max_count = max(freq_arr_summed)
    for i in range(0, len(freq_arr_summed)):
        if freq_arr_summed[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns


if __name__ == '__main__':
    test_seq = 'AAGCAAAGGTGGG'
    with open('chapter_1/inputs/freq_words_mismatch_rev_compl.txt', 'r') as in_f:
        text, stuff = in_f.read().strip().split('\n')
        k, d = stuff.strip().split(' ')
        print(' '.join([x for x in faster_frequent_words_with_mismatches(text, int(k), int(d))]))
