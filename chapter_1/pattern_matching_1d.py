def find_pattern_matches(pattern: str, genome: str) -> list[int]:
    return list(filter(lambda x: x is not None, 
        [idx if genome[idx:idx+len(pattern)] == pattern else None for idx in range(0, len(genome)-len(pattern)+1)]))


if __name__ == '__main__':
    test_seq = 'ATGCATGCATGC'

    with open('chapter_1/inputs/pattern_indices.txt', 'r') as in_fh:
        ptrn, gen = in_fh.read().split('\n')
        print(' '.join([str(x) for x in find_pattern_matches(ptrn, gen)]))