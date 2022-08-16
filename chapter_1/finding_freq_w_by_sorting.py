from pattern_to_number_1l import pattern_to_number
from number_to_pattern_1m import number_to_pattern

import time
start_time = time.time()

def find_freq_words_by_sorting(text: str, k: int) -> set:
    # find patterns
    freq_patterns = set()
    indices = []
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        indices.append(pattern_to_number(pattern))
    counts = [1] * len(indices)

    # sort array and fill the counts array appropriately
    indices.sort()
    for i in range(1, len(text) - k):
        if indices[i] == indices[i-1]:
            counts[i] = counts[i-1] + 1
    
    # find patterns with highest counts
    max_count = max(counts)
    for i, el in enumerate(indices):
        if counts[i] == max_count:
            freq_patterns.add(number_to_pattern(el, k))
    
    return freq_patterns


if __name__ == '__main__':
    '''
    test_seq = 'AAGCAAAGGTGG'
    test_k = 2
    print(find_freq_words_by_sorting(test_seq, test_k))
    '''
    with open('chapter_1/inputs/frequent_words.txt', 'r') as in_f:
        text = in_f.read().split('\n')
        for i in range(0, 100):
            find_freq_words_by_sorting(text=text[0], k=int(text[1]))

    print("SORTING FREQ WORDS: --- %s seconds ---" % (time.time() - start_time))