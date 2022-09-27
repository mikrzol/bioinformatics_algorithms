from random import choice

def create_graph_from_file(text: list[str], balance: bool = True) -> tuple[dict, int, int] | dict:
    graph = {}
    for line in text:
        line = line.strip().split(' -> ')
        if line[0] not in graph.keys():
            graph[line[0]] = [[], 0, 0] # neighs, in_deg, out_deg 
        neighs = line[1].split(',')
        for neigh in neighs:
            graph[line[0]][0].append(neigh)
            graph[line[0]][2] += 1
            if neigh not in graph.keys():
                graph[neigh] = [[], 0, 0]
            graph[neigh][1] += 1
    
    if balance:
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
    else:
        return graph


def recreate_cycle_from_idx(my_list: list, idx: int) -> list:
    l = my_list[:-1]
    my_list_len = len(my_list) - 1
    new_l= [l[i%my_list_len] for i in range(idx, idx+my_list_len)]
    new_l.append(new_l[0])
    return new_l


def eulerian_path(graph: dict, in_deg_missing, out_deg_missing) -> list[str]:
    """
    Find Eulerian path in a graph by appending a missing edge to a nearly balanced graph.
    
    !!! The graph is assumed to have an Eulerian path !!!
    """
    # form a cycle by randomly walking in graph (don't visit the same edge twice!)
    curr = choice(list(graph.keys()))
    total_edges = sum([len(graph[node][0]) for node in graph.keys()])
    remaining_edges_num = total_edges
    cycle = [curr]

    # traverse graph
    while True:
        if len(graph[curr][0]) == 0:   # no neighbors -> we got 'stuck'
            break
        # choose a dest from neighbors
        dest = choice(graph[curr][0])
        # add dest to cycle
        cycle.append(dest)
        # remove edge from graph
        graph[curr][0].remove(dest)
        remaining_edges_num -= 1
        # move to dest
        curr = dest

    while remaining_edges_num > 0:  # there are unused edges left
        # get first node that: 1) has unused edges, 2) is in cycle
        for i, node in enumerate(cycle):
            if len(graph[node][0]) > 0:
                curr = node
                cycle = recreate_cycle_from_idx(cycle, i)
                break

        while True:
            if len(graph[curr][0]) == 0:   # no neighbors -> we got 'stuck'
                break
            dest = choice(graph[curr][0])
            cycle.append(dest)
            graph[curr][0].remove(dest)
            remaining_edges_num -= 1
            curr = dest

    path = cycle[0:-1]
    # rotate until the missing edge matches end and beginning
    while path[0] != in_deg_missing or path[-1] != out_deg_missing:  
       path.append(path.pop(0))

    return path


def main():
    with open('chapter_3/inputs/rosalind_ba3g.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        graph, in_deg_missing, out_deg_missing = create_graph_from_file(text)
        res = '->'.join(eulerian_path(graph, in_deg_missing, out_deg_missing))
        with open('chapter_3/res.txt', 'w') as out_fh:
            out_fh.write(res)


if __name__ == '__main__':
    main()