import time

def my_find_words_repeated_t_times(seq: str, k: int, t: int) -> set[str]:
    all_patterns = {}
    for i in range(0, len(seq) - k):
        if seq[i:i+k] in all_patterns.keys():
            all_patterns[seq[i:i+k]] += 1
        else:
            all_patterns[seq[i:i+k]] = 1
    
    freq_patterns = set()
    for key, val in all_patterns.items():
        if val >= t:
            freq_patterns.add(key)

    return freq_patterns


def my_clump_finder(genome: str, k: int, L: int, t: int) -> set[str]:
    clumps = set()
    for i in range(0, len(genome)-L+1):
        clumps = clumps | my_find_words_repeated_t_times(genome[i:i+L], k, t)
    return clumps


if __name__ == '__main__':
    '''test_genome = 'GATCAGCATAAGGGTCCCTGCAATGCATGACAAGCCTGCAGTTGTTTTAC'
    start_time = time.time()
    for i in range(0, 100):
        my_clump_finder(test_genome, 4, 25, 3)
    print("MY CLUMP FINDER: --- %s seconds ---" % (time.time() - start_time))'''
    with open('chapter_1/inputs/clumps.txt', 'r') as in_fh:
        gen, stuff = in_fh.read().split('\n')
        k, L, t = stuff.split(' ')
        print(' '.join(my_clump_finder(gen, int(k), int(L), int(t))))