from pattern_to_number_1l import pattern_to_number
from number_to_pattern_1m import number_to_pattern
from neighbors_1n import neighbors
# import time
# from tqdm import tqdm

def computing_freqs_w_mismatches(text: str, k: int, d: int) -> set[str]:
    freq_arr = [0] * (4**k)

    for i in range(0, len(text) - k + 1):
        neighborhood = neighbors(text[i:i+k], d)
        for approx_pattern in neighborhood:
            j = pattern_to_number(approx_pattern)
            freq_arr[j] += 1

    return freq_arr

def faster_frequent_words_with_mismatches(text: str, k: int, d: int) -> set[str]:
    '''
    text:   sequence to find frequent words in
    k:      length of k-mer
    d:      number of allowed mismatches (Hamming distance)
    '''
    frequent_patterns = set()
    frequency_array = computing_freqs_w_mismatches(text, k, d)

    max_count = max(frequency_array)
    for i in range(0, 4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns


if __name__ == '__main__':
    test_seq = 'AAGCAAAGGTGGG'
    with open('chapter_1/inputs/frequent_words_mismatches.txt', 'r') as in_f:
        text, stuff = in_f.read().split('\n')
        k, d = stuff.strip().split(' ')
        print(' '.join([x for x in faster_frequent_words_with_mismatches(text, int(k), int(d))]))
