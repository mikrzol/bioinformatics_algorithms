def hamming_distance(str1: str, str2: str) -> int:
    '''
    if len(str1) != len(str2):
        print('Strings must have equal length')
        return
    '''
    hamming_distance = 0
    for el1, el2 in zip(str1, str2):
        if el1 != el2:
            hamming_distance += 1
    return hamming_distance


if __name__ == '__main__':
    test_seq1 = 'mikrz'
    test_seq2 = 'mokry'
    with open('chapter_1/inputs/hamming_dist.txt', 'r') as in_fh:
        seq1, seq2 = in_fh.read().strip().split('\n')
        print(hamming_distance(seq1, seq2))