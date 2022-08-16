from computing_frequencies_1k import computing_frequencies
from number_to_pattern_1m import number_to_pattern

import time
start_time = time.time()

def faster_frequent_words(text: str, k: int) -> set[str]:
    frequent_patterns = set()
    frequency_array = computing_frequencies(text, k)

    max_count = max(frequency_array)
    for i in range(0, 4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns


if __name__ == '__main__':
    with open('chapter_1/inputs/frequent_words.txt', 'r') as in_f:
        text = in_f.read().split('\n')
        for i in range(0, 100):
            faster_frequent_words(text=text[0], k=int(text[1]))

    print("FASTER FREQ WORDS: --- %s seconds ---" % (time.time() - start_time))