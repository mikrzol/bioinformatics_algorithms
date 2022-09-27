from chapter_3.string_from_path_3b import string_from_path

def string_spelled_by_gapped_patterns(gapped_ptrns: list[str], k: int, d: int, from_file: bool = False) -> str:
    # when input from file
    if from_file:
        first_patterns = [x.strip().split('|')[0] for x in gapped_ptrns]
        second_patterns = [x.strip().split('|')[1] for x in gapped_ptrns]
    else:
        first_patterns = [x[0] for x in gapped_ptrns]
        second_patterns = [x[1] for x in gapped_ptrns]

    prefix_string = string_from_path(first_patterns)
    suffix_string = string_from_path(second_patterns)
    for i in range(k+d, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return 'there is no string spelled by the gapped patterns'
    return prefix_string + suffix_string[-(k+d):]


def main():
    '''
    test_k, test_d = 4, 2
    test_gapped_patterns = [
    'GACC|GCGC',
    'ACCG|CGCC',
    'CCGA|GCCG',
    'CGAG|CCGG',
    'GAGC|CGGA'
    ]
    print(string_spelled_by_gapped_patterns(test_gapped_patterns, test_k, test_d, from_file=True))

    with open('chapter_3/inputs/string_spelled_by_gapped_patterns.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('Output')
        inputs = text[0].strip().split('\n')[1:]
        k, d = map(int, inputs[0].strip().split(' '))
        gapped_patterns = inputs[1:]
        
        output = text[1].strip()
        print(string_spelled_by_gapped_patterns(gapped_patterns, k, d, from_file=True) == output)
    '''
    with open('chapter_3/inputs/rosalind_ba3l.txt', 'r') as in_fh:
        inputs = in_fh.read().strip().split('\n')
        k, d = map(int, inputs[0].split(' '))
        gapped_patterns = inputs[1:]
        print(string_spelled_by_gapped_patterns(gapped_patterns, k, d, from_file=True))


if __name__ == '__main__':
    main()