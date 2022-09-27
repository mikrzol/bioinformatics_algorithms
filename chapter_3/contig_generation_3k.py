import sys
from chapter_3.maximal_non_branching_paths_3m import maximal_non_branching_paths

def create_de_bruijn_graph(patterns: list[str]) -> dict:
    graph = {}
    for line in patterns:
        src = line[:-1]
        dest = line[1:]
        if src not in graph.keys():
            graph[src] = [[], 0, 0]     # neighs, in_deg, out_deg 
        graph[src][0].append(dest)
        graph[src][2] += 1
        if dest not in graph.keys():
            graph[dest] = [[], 0, 0]    # neighs, in_deg, out_deg 
        graph[dest][1] += 1

    return graph


def generate_contigs(patterns: list[str]) -> list[str]:
    graph = create_de_bruijn_graph(patterns)
    return maximal_non_branching_paths(graph)


def main():
    
    with open('chapter_3/inputs/rosalind_ba3k.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        contigs = generate_contigs(text)
        for contig in contigs:
            print(contig[0] + ''.join(x[-1] for x in contig[1:]))
    '''
    with open('chapter_3/inputs/contig_generation.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('Output:')
        inputs = text[0].strip().split('\n')[1:]

        sys.setrecursionlimit(len(inputs))  # need to increase limit of recursion for dfs implementation

        contigs = generate_contigs(inputs)

        output = sorted(text[1].strip().split('\n'))
        res = [contig[0] + ''.join(x[-1] for x in contig[1:]) for contig in contigs]
        res.sort()

        print(res == output)
    '''


if __name__ == '__main__':
    main()