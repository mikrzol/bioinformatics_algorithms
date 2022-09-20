from chapter_3.eulerian_path_3g import eulerian_path

def de_bruijn_graph_from_file(patterns: list[str]) -> tuple[dict, int, int]:
    graph = {}
    for pattern in patterns:
        if pattern[:-1] not in graph.keys():
            graph[pattern[:-1]] = [[], 0 , 0] # neighs, in_deg, out_deg
        if pattern[1:] not in graph.keys():
            graph[pattern[1:]] = [[], 0, 0] # neighs, in_deg, out_deg
        
        # add target to neighs of source
        graph[pattern[:-1]][0].append(pattern[1:])
        graph[pattern[:-1]][0].sort()
        # increment out_deg of source
        graph[pattern[:-1]][2] += 1
        # increment in_deg of target
        graph[pattern[1:]][1] += 1

    # find the unbalanced nodes and balance them
    out_deg_missing = None
    in_deg_missing = None
    for key in graph.keys():
        if graph[key][1] > graph[key][2]:
            out_deg_missing = key
            graph[key][2] += 1
        elif graph[key][2] > graph[key][1]:
            in_deg_missing = key
            graph[key][1] += 1

    graph[out_deg_missing][0].append(in_deg_missing)
    return (graph, in_deg_missing, out_deg_missing)


if __name__ == '__main__':
    with open('chapter_3/inputs/rosalind_ba3h.txt', 'r') as in_fh:
        
        text = in_fh.read().strip().split('\n')[1:]
        graph, in_deg_missing, out_deg_missing = de_bruijn_graph_from_file(text)
        res = eulerian_path(graph, in_deg_missing, out_deg_missing)
        print(res[0] + ''.join([x[-1] for x in res[1:]]))
        '''
        text = in_fh.read().strip().split('Output:')
        input = text[0].strip().split('\n')[2:]
        answer = text[1].strip()
        graph, in_deg_missing, out_deg_missing = de_bruijn_graph_from_file(input)
        res = eulerian_path(graph, in_deg_missing, out_deg_missing)
        final_res = res[0] + ''.join([x[-1] for x in res[1:]])
        print(f'RES:\n{final_res}')
        print(f'ANSWER:\n{answer}')
        print(final_res == answer)
        '''
