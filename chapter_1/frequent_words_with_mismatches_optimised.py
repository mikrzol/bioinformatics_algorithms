from neighbors_1n import neighbors
from pattern_to_number_1l import pattern_to_number
from number_to_pattern_1m import number_to_pattern
# import time
# from tqdm import tqdm

def find_freq_w_mismatches_sorting(text: str, k: int, d: int) -> set[str]:
    frequent_patterns = set()
    neighborhoods = []

    for i in range(0, len(text) - k + 1):
        neighborhoods.extend(neighbors(text[i:i+k], d))
    
    # form an array neighborhood_arr holding all strings in neighborhoods
    neighborhood_arr = list(neighborhoods)

    count = [0] * (len(neighborhoods))
    index = [0] * (len(neighborhoods))
    for i in range(0, len(neighborhoods)):
        index[i] = pattern_to_number(neighborhood_arr[i])
        count[i] = 1

    index.sort()

    for i in range(0, len(neighborhoods) - 1):
        if index[i] == index[i+1]:
            count[i+1] = count[i] + 1

    max_count = max(count)
    for i in range(0, len(neighborhoods)):
        if count[i] == max_count:
            frequent_patterns.add(number_to_pattern(index[i], k))
    
    return frequent_patterns


if __name__ == '__main__':
    test_seq = 'AAGCAAAGGTGGG'

    with open('chapter_1/inputs/frequent_words_mismatches.txt', 'r') as in_f:
        text, stuff = in_f.read().split('\n')
        k, d = stuff.strip().split(' ')
        print(' '.join([x for x in find_freq_w_mismatches_sorting(text, int(k), int(d))]))
