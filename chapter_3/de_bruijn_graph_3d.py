def de_bruijn_graph(seq: str, k: int) -> dict:
    kmers = [seq[i:i+k-1] for i in range(len(seq) - k + 2)]
    graph = {}
    for i in range(len(kmers)-1):     # not range +1 because we go up to the second last kmer 
        if kmers[i] not in graph.keys():
            graph[kmers[i]] = []
        graph[kmers[i]].append(kmers[i+1])
        graph[kmers[i]].sort()
    
    return graph


def print_de_bruijn_graph(graph: dict) -> None:
    # sort only for rosalind to accept answer
    for key in sorted(graph.keys()):
        print(f"{key} -> {','.join(graph[key])}")


def format_de_bruijn_graph(graph: dict):
    return [f"{key} -> {','.join(graph[key])}" for key in sorted(graph.keys())]



if __name__ == '__main__':
    test_k = 4
    test_seq = 'AAGATTCTCTAC'
    # print_de_bruijn_graph(de_bruijn_graph(test_seq, test_k))
    '''
    with open('chapter_3/inputs/De_Bruijn_Graph_from_a_String.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k = int(text[1])
        seq = text[2]
        answer = text[4:]
        print(format_de_bruijn_graph(de_bruijn_graph(seq, k)) == answer)
    '''
    with open('chapter_3/inputs/rosalind_ba3d.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k = int(text[0])
        seq = text[1]
        with open('chapter_3/res.txt', 'w') as out_fh:
            out_fh.write('\n'.join(format_de_bruijn_graph(de_bruijn_graph(seq, k))))
