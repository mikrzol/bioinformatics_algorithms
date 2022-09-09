from chapter_3.de_bruijn_graph_3d import print_de_bruijn_graph, format_de_bruijn_graph

def de_bruijn_graph_from_kmers(patterns: list[str]) -> dict:
    graph = {}
    for pattern in patterns:
        if pattern[:-1] not in graph.keys():
            graph[pattern[:-1]] = []
        '''
        if pattern[1:] not in graph.keys():
            graph[pattern[1:]] = []
        '''
        graph[pattern[:-1]].append(pattern[1:])
        graph[pattern[:-1]].sort()
            
    return graph


if __name__ == '__main__':
    test_patterns = [
        'GAGG',
        'CAGG',
        'GGGG',
        'GGGA',
        'CAGG',
        'AGGG',
        'GGAG'
    ]
    test_patterns_2 = [
        'AAT',
        'ATG',
        'ATG',
        'ATG',
        'CAT',
        'CCA',
        'GAT',
        'GCC',
        'GGA',
        'GGG',
        'GTT',
        'TAA',
        'TGC',
        'TGG',
        'TGT'
    ]
    print_de_bruijn_graph(de_bruijn_graph_from_kmers(test_patterns))
    '''
    with open('chapter_3/inputs/rosalind_ba3e.txt', 'r') as in_fh:
        patterns = in_fh.read().strip().split('\n')
        with open('chapter_3/res.txt', 'w') as out_fh:
            out_fh.write('\n'.join(format_de_bruijn_graph(de_bruijn_graph_from_kmers(patterns))))
    '''
