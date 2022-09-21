from chapter_3.de_bruijn_from_kmers_3e import de_bruijn_graph_from_kmers
from chapter_3.eulerian_cycle_3f import eulerian_cycle
from itertools import product

def k_universal_circ_bin_string(k: int) -> str:
    all_kmers = [''.join(x) for x in product('01', repeat=k)]
    graph = de_bruijn_graph_from_kmers(all_kmers)
    cycle = eulerian_cycle(graph)[:-(k-1)]

    return cycle[0] + ''.join([x[-1] for x in cycle[1:]])


def main():
    res = k_universal_circ_bin_string(9)
    
    print(res)


if __name__ == '__main__':
    main()