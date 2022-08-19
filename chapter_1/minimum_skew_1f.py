def find_minimum_skew(genome: str) -> list[int]:
    skew = [0] * (len(genome)+1)

    minimum = 0
    for i, nucl in enumerate(genome):
        skew[i+1] = skew[i]
        if nucl == 'G':
            skew[i+1] += 1
        elif nucl == 'C':
            skew[i+1] -= 1
        if skew[i+1] < minimum:
            minimum = skew[i+1]

    print(skew[40:60])
    print(skew[62:68])
    print(skew[80:100])
    print(min(skew))
    

    return list(filter(lambda x: x is not None, 
        [idx if skew[idx] == minimum else None for idx, _ in enumerate(skew)]))


if __name__ == '__main__':
    test_genome = 'CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'
    with open('chapter_1/inputs/GCF_003018455.1_ASM301845v1_genomic.fna', 'r') as in_fh:
        genome = ''.join([x for x in in_fh.read().strip().split('>')[1].split('\n')[1:]])
        print(' '.join([str(x) for x in find_minimum_skew(genome)]))