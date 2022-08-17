complementary_nucls_dna = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
    'N': 'N',
}

def reverse_complement(seq: str) -> str:
    # remember to revert the string
    return ''.join([complementary_nucls_dna[nucl] for nucl in seq.upper()])[::-1]


if __name__ == '__main__':
    test_seq = 'agtcgcatagt'
    test_seq2 = 'AAAACCCGGT'
    with open('./chapter_1/inputs/reverse_complement.txt', 'r') as in_f:
        print(reverse_complement(in_f.read().strip()))