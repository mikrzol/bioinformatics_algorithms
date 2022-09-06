def string_composition(seq: str, k: int) -> list[str]:
    return sorted([seq[i:i+k] for i in range(len(seq) - k + 1)])


if __name__ == '__main__':
    test_seq = 'TATGGGGTGC'
    with open('chapter_3/inputs/string_comp.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        k = int(text[0])
        seq = text[1]
        with open('chapter_3/res.txt', 'w') as out_fh:
            out_fh.write('\n'.join(string_composition(seq, k)))
