import matplotlib.pyplot as plt

def plot_skew(genome: str) -> list[int]:
    skew = [0] * (len(genome)+1)
    for i, nucl in enumerate(genome):
        skew[i+1] = skew[i]
        if nucl == 'G':
            skew[i+1] += 1
        elif nucl == 'C':
            skew[i+1] -= 1
    
    plt.plot(skew)
    plt.title('Skew plot')
    plt.xlabel('position')
    plt.ylabel('skew (G-C)')
    plt.savefig('chapter_1/plots/skew.jpg')


if __name__ == '__main__':
    test_genome = 'CATGGGCATCGGCCATACGCC'
    with open('chapter_1/inputs/GCF_003018455.1_ASM301845v1_genomic.fna', 'r') as in_fh:
        genome = ''.join([x for x in in_fh.read().strip().split('>')[1].split('\n')[1:]])
        plot_skew(genome)