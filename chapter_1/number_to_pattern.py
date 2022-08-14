number_to_symbol = {
    0: "A",
    1: "C",
    2: "G",
    3: "T"
}

def number_to_pattern(index: int, k: int) -> str:
    if index == 0:
        return ''
    if k == 1:
        return number_to_symbol[index]
    ''' STEP BY STEP EXPLANATION:
    prefix_index = index // 4
    r = index % 4
    symbol = number_to_symbol[r]
    prefix_pattern = number_to_pattern(prefix_index, k-1)
    return prefix_pattern + symbol
    '''
    return number_to_pattern(index // 4, k-1) + number_to_symbol[index % 4]


if __name__ == '__main__':
    print(number_to_pattern(5437, 8))