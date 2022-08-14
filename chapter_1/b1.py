# FREQUENT WORDS
from a1 import pattern_count

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
    txt1 = 'ACTGACTCCCACCCG'

    print(frequent_words(txt1, 3))