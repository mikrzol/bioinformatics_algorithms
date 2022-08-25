from cmath import inf

from chapter_1.number_to_pattern_1m import number_to_pattern
from chapter_2.distance_pattern_string_2h import distance_between_pattern_and_string

def median_string(dna_seqs: list[str], k: int) -> str:
    distance = inf
    med = ''

    for i in range(0, 4**k):
        pattern = number_to_pattern(i, k)
        if distance > distance_between_pattern_and_string(pattern, dna_seqs):
            distance = distance_between_pattern_and_string(pattern, dna_seqs)
            med = pattern
        
    return med


if __name__ == '__main__':
    '''
    test_dna_seqs = [
        'TTACCTTAAC',
        'GATATCTGTC',
        'ACGGCGTTCG',
        'CCCTAAAGAG',
        'CGTCAGAGGT'
    ]
    test_k = 3
    '''
    with open('chapter_2/inputs/median_string.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k = int(text[0])
        dna_seqs = text[1:]
        print(median_string(dna_seqs, k))

