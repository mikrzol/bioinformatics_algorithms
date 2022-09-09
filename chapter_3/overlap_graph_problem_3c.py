def create_overlap_graph(patterns: list[str]) -> list[str]:
    adj_list = {}
    patterns = sorted(patterns)
    for pattern in patterns:
        adj_list[pattern] = []
        for n in patterns:
            if pattern[1:] == n[:-1]:
                adj_list[pattern].append(n)
    return adj_list


def format_adj_graph(graph: dict):
    res = []
    for node in graph:
        for neigh in graph[node]:
            res.append(f'{node} -> {neigh}')
    return res


if __name__ == '__main__':
    test_ptrns = [
        'ATGCG',
        'GCATG',
        'CATGC',
        'AGGCA',
        'GGCAT'
    ]
    print(create_overlap_graph(test_ptrns))
    '''
    with open('chapter_3/inputs/rosalind_ba3c.txt', 'r') as in_fh:
        ptrns = in_fh.read().strip().split('\n')
        with open('chapter_3/res.txt', 'w') as out_fh:
            out_fh.write('\n'.join(format_adj_graph(create_overlap_graph(ptrns))))
    '''