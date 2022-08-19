from hamming_distance_1g import hamming_distance

def neighbors(pattern: str, d: int) -> set[str]:
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighborhood = set()
    suffix_neighs = neighbors(pattern[1:], d)

    for neighbor in suffix_neighs:
        if hamming_distance(pattern[1:], neighbor) < d:
            for nucl in ['A', 'C', 'G', 'T']:
                neighborhood.add(nucl + neighbor)
        else:
            neighborhood.add(pattern[0] + neighbor)
    
    return neighborhood


if __name__ == '__main__':
    test_seq = 'CAA'

    with open('chapter_1/inputs/neighborhood.txt', 'r') as in_fh:
        pattern, d = in_fh.read().strip().split('\n')
        with open('res.txt', 'w') as out_fh:
            out_fh.write('\n'.join(neighbors(pattern, int(d))))
