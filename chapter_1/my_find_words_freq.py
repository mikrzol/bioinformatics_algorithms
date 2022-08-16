import time
start_time = time.time()

def my_find_words(text: str, k: int) -> set[str]:
    all_patterns = {}
    for i in range(0, len(text) - k):
        if text[i:i+k] in all_patterns.keys():
            all_patterns[text[i:i+k]] += 1
        else:
            all_patterns[text[i:i+k]] = 1
    
    max_count = max(all_patterns.values())
    freq_patterns = set()
    for key, val in all_patterns.items():
        if val == max_count:
            freq_patterns.add(key)

    return freq_patterns

if __name__ == '__main__':
    with open('chapter_1/inputs/frequent_words.txt', 'r') as in_f:
        text = in_f.read().split('\n')
        for i in range(0, 100):
            my_find_words(text=text[0], k=int(text[1]))

    print("MY FREQ WORDS: --- %s seconds ---" % (time.time() - start_time))