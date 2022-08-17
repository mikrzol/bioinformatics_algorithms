from computing_frequencies_1k import computing_frequencies
from number_to_pattern_1m import number_to_pattern
import time

def clump_finder(genome: str, k: int, L: int, t: int) -> set[str]:
    freq_patterns = set()
    clump = [0] * (4**k - 1)

    for i in range(len(genome) - L + 1):
        freq_arr = computing_frequencies(genome[i:i+L], k)
        for j in range(0, len(clump)):
            if freq_arr[j] >= t:
                clump[j] = 1
    
    for i, el in enumerate(clump):
        if el:
            freq_patterns.add(number_to_pattern(i, k))
    
    return freq_patterns


if __name__ == '__main__':
    test_genome = 'GATCAGCATAAGGGTCCCTGCAATGCATGACAAGCCTGCAGTTGTTTTAC'
    start_time = time.time()
    for i in range(0, 100):
        clump_finder(test_genome, 4, 25, 3)
    print("NAIVE CLUMP FINDER: --- %s seconds ---" % (time.time() - start_time))