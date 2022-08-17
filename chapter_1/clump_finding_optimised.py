from computing_frequencies_1k import computing_frequencies
from number_to_pattern_1m import number_to_pattern
from pattern_to_number_1l import pattern_to_number
import time

def clump_finder_optimised(genome: str, k: int, L: int, t: int) -> set[str]:
    freq_patterns = set()
    clump = [0] * (4**k - 1)

    freq_arr = computing_frequencies(genome[0:L], k)
    for i in range(0, len(clump)):
        if freq_arr[i] >= t:
            clump[i] = 1
    
    for i in range(1, len(genome)-L):
        first_pattern = genome[i-1:i-1+k]
        index = pattern_to_number(first_pattern)
        freq_arr[index] = freq_arr[index] - 1
        
        last_pattern = genome[i+L-k:i+L]
        index = pattern_to_number(last_pattern)
        freq_arr[index] = freq_arr[index] + 1

        if freq_arr[index] >= t:
            clump[index] = 1
    
    for i, el in enumerate(clump):
        if el:
            freq_patterns.add(number_to_pattern(i, k))
    
    return freq_patterns


if __name__ == '__main__':
    '''
    test_genome = 'GATCAGCATAAGGGTCCCTGCAATGCATGACAAGCCTGCAGTTGTTTTAC'
    start_time = time.time()
    for i in range(0, 1000):
        clump_finder_optimised(test_genome, 4, 25, 3)
    print("OPTIMISED CLUMP FINDER: --- %s seconds ---" % (time.time() - start_time))
    '''
    with open('chapter_1/inputs/clumps.txt', 'r') as in_fh:
        gen, stuff = in_fh.read().split('\n')
        k, L, t = stuff.split(' ')
        print(' '.join(clump_finder_optimised(gen, int(k), int(L), int(t))))