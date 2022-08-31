import cProfile
import pstats
from chapter_2.greedy_motif_search_2d import greedy_motif_search    # example function to track

k, t = 0, 0
dna_seqs = []

# get args for the function
with open('chapter_2/inputs/greedy_motif_laplace.txt', 'r') as in_fh:
    text = in_fh.read().strip().split('\n')
    k, t = map(int, text[0].strip().split(' '))
    dna_seqs = text[1:]
    # print(' '.join(greedy_motif_search(dna_seqs, k, t, laplace_succession=True)))

# create a profile
profile = cProfile.Profile()

# run the function
profile.runcall(greedy_motif_search, k=k, t=t, dna_seqs = dna_seqs, laplace_succession=True)

# generate the stats
ps = pstats.Stats(profile)

# sort stats
ps.sort_stats('cumtime', 'ncalls')

# print the stats (n top results after sorting)
ps.print_stats(10)