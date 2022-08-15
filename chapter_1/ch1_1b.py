# FREQUENT WORDS
from ch1_1a import pattern_count

def frequent_words(text: str, k: int) -> list:
    all_patterns = {}
    for i in range(0, len(text) - k):
        all_patterns[text[i:i+k]] = pattern_count(text, text[i:i+k])
    
    max_count = max(all_patterns.values())
    frequent_patterns = set()
    for key, val in all_patterns.items():
        if val == max_count:
            frequent_patterns.add(key)
    
    return frequent_patterns

if __name__ == '__main__':
    with open('chapter_1/in_f.txt', 'r') as in_f:
        text = in_f.read().split('\n')
        print(frequent_words(text=text[0], k=int(text[1])))