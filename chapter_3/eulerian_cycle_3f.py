from random import choice

def create_graph_from_file(text: list[str]) -> None:
    graph = {}
    for line in text:
        line = line.strip().split(' -> ')
        graph[line[0]] = []
        neighs = line[1].split(',')
        for neigh in neighs:
            graph[line[0]].append(neigh)
            if neigh not in graph.keys():
                graph[neigh] = []
    
    return graph


def recreate_cycle_from_idx(my_list: list, idx: int) -> list:
    l = my_list[:-1]
    my_list_len = len(my_list) - 1
    new_l= [l[i%my_list_len] for i in range(idx, idx+my_list_len)]
    new_l.append(new_l[0])
    return new_l


def eulerian_cycle(graph: dict) -> list[str]:
    """
    Find Eulerian cycle in a graph.
    
    !!! The graph is assumed BALANCED and STRONGLY CONNECTED !!!
    """
    # form a cycle by randomly walking in graph (don't visit the same edge twice!)
    curr = choice(list(graph.keys()))
    total_edges = sum([len(graph[node]) for node in graph.keys()])
    remaining_edges_num = total_edges
    cycle = [curr]

    # traverse graph
    while True:
        if len(graph[curr]) == 0:   # no neighbors -> we got 'stuck'
            break
        # choose a dest from neighbors
        dest = choice(graph[curr])
        # add dest to cycle
        cycle.append(dest)
        # remove edge from graph
        graph[curr].remove(dest)
        remaining_edges_num -= 1
        # move to dest
        curr = dest
    

    while remaining_edges_num > 0:  # there are unused edges left
        # get first node that: 1) has unused edges, 2) is in cycle
        for i, node in enumerate(cycle):
            if len(graph[node]) > 0:
                curr = node
                cycle = recreate_cycle_from_idx(cycle, i)
                break
        
        while True:
            if len(graph[curr]) == 0:   # no neighbors -> we got 'stuck'
                break
            dest = choice(graph[curr])
            cycle.append(dest)
            graph[curr].remove(dest)
            remaining_edges_num -= 1
            curr = dest

    return cycle


def main():
    with open('chapter_3/inputs/rosalind_ba3f.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        graph = create_graph_from_file(text)
        with open('chapter_3/res.txt', 'w') as out_fh:
            out_fh.write('->'.join(eulerian_cycle(graph)))
    

if __name__ == '__main__':
    main()