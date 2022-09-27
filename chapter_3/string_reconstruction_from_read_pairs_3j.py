from chapter_3.eulerian_path_3g import eulerian_path
from chapter_3.string_spelled_by_gapped_patterns_3l import string_spelled_by_gapped_patterns

def de_bruin_graph_from_read_pairs(nodes: list[str]) -> tuple:
    graph = {}
    for node in nodes:
        n = node.strip().split('|')
        if (n[0][:-1], n[1][:-1]) not in graph.keys():
            graph[(n[0][:-1], n[1][:-1])] = [[], 0 , 0] # neighs, in_deg, out_deg
        if (n[0][1:], n[1][1:]) not in graph.keys():
            graph[(n[0][1:], n[1][1:])] = [[], 0 , 0] # neighs, in_deg, out_deg
        # add target to neighs of source
        graph[(n[0][:-1], n[1][:-1])][0].append((n[0][1:], n[1][1:]))
        # increment out_deg of source
        graph[(n[0][:-1], n[1][:-1])][2] += 1
        # increment in_deg of target
        graph[(n[0][1:], n[1][1:])][1] += 1

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


def main():
    with open('chapter_3/inputs/rosalind_ba3j.txt', 'r') as in_fh:
        '''
        text = in_fh.read().strip().split('Output')
        inputs = text[0].strip().split('\n')[1:]
        k, d = map(int, inputs[0].strip().split(' '))
        graph, in_deg_missing, out_deg_missing = de_bruin_graph_from_read_pairs(inputs[1:])
        res = eulerian_path(graph, in_deg_missing, out_deg_missing)

        output = text[1].strip()
        
        print(string_spelled_by_gapped_patterns(res, k, d) == output)
        '''
        text = in_fh.read().strip().split('\n')
        k, d = map(int, text[0].strip().split(' '))
        graph, in_deg_missing, out_deg_missing = de_bruin_graph_from_read_pairs(text[1:])
        res = eulerian_path(graph, in_deg_missing, out_deg_missing)
        print(string_spelled_by_gapped_patterns(res, k, d))


if __name__ == '__main__':
    main()