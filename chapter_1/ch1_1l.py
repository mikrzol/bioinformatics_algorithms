symbol_to_number = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

def pattern_to_number(pattern: str) -> int:
    if not pattern:
        return 0
    symbol = pattern[-1]
    prefix = pattern[0:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number[symbol]


if __name__ == '__main__':
    print(pattern_to_number('CGAAATTCGCAACCAGTCGGGAAT'))