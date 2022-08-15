from ch1_1k import computing_frequencies
from ch1_1m import number_to_pattern

def faster_frequent_words(text: str, k: int) -> set:
    frequent_patterns = set()
    frequency_array = computing_frequencies(text, k)

    max_count = max(frequency_array)
    for i in range(0, 4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns


if __name__ == '__main__':
    with open('chapter_1/in_f.txt', 'r') as in_f:
        text = in_f.read().split('\n')
        print(faster_frequent_words(text=text[0], k=int(text[1])))