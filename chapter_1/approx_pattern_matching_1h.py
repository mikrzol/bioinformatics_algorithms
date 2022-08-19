from hamming_distance_1g import hamming_distance

def approx_pattern_matching(text: str, pattern: str, d: int) -> list[int]:
    indices = []
    for i in range(0, len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i+len(pattern)], pattern) <= d:
            indices.append(i)
    
    return indices


if __name__ == '__main__':
    test_seq = 'AACAAGCATAAACATTAAAGAG'
    test_ptrn = 'AAAAA'
    with open('chapter_1/inputs/approx_pattern_match.txt', 'r') as in_fh:
        pattern, text, d = in_fh.read().strip().split('\n')
        print(' '.join([str(x) for x in approx_pattern_matching(text, pattern, int(d))]))