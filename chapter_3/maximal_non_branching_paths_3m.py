from chapter_3.eulerian_path_3g import create_graph_from_file

def maximal_non_branching_paths(graph: dict) -> list:
    def dfs(visited: set, graph: dict, node) -> None:
        stack = [node]

        while stack:
            s = stack.pop()
            if s not in visited:
                visited.add(s)
                for neighbour in graph[s][0]:
                    stack.append(neighbour)
        '''
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node][0]:
                dfs(visited, graph, neighbour)
        '''


    def find_non_branching_paths(graph: dict, paths: list) -> None:
        for node in graph.keys():
            if graph[node][1] != 1 or graph[node][2] != 1:
                if graph[node][2] > 0:
                    for dest in graph[node][0]:
                        non_branching_path = [node, dest]
                        while graph[dest][1] == 1 and graph[dest][2] == 1 :
                            dest = graph[dest][0][0]    # first (and only) neighbour
                            non_branching_path += [dest]
                        paths.append(non_branching_path)


    def find_isolated_cycles(graph: dict, paths: list) -> None:
        cycle_candidates = []
        # determine if node is in isolated subgraph
        for node in graph.keys():
            visited = set()
            dfs(visited, graph, node)
            if len(visited) < len(list(graph.keys())):
                cycle_candidates.append(node)

        for candidate in cycle_candidates:
            curr = candidate
            cycle = []
            while graph[curr][1] == 1 and graph[curr][2] == 1:
                cycle.append(curr)
                curr = graph[curr][0][0]    # first (and only) neighbour
                if curr == candidate:
                    # remove nodes from this cycle from candidates (prevent duplicates)
                    for node in cycle:
                        cycle_candidates.remove(node)
                    
                    # close the cycle
                    cycle.append(curr)
                    # add cycle to paths
                    paths.append(cycle)

                    break

    paths = []
    find_non_branching_paths(graph, paths)
    find_isolated_cycles(graph, paths)
    return paths


def main():
    
    with open('chapter_3/inputs/rosalind_ba3m.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        graph = create_graph_from_file(text, balance=False)
        paths = maximal_non_branching_paths(graph)
        for path in paths:
            print(' -> '.join(path))
    '''
    with open('chapter_3/inputs/maximal_nonbranching_paths (1).txt', 'r') as in_fh:
        text = in_fh.read().strip().split('Output')
        inputs = text[0].strip().split('\n')[1:]
        graph = create_graph_from_file(inputs, balance=False)
        paths = maximal_non_branching_paths(graph)
        for path in paths:
            print(' -> '.join(path))
    '''


if __name__ == '__main__':
    main()