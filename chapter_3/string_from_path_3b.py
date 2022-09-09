def string_from_path(kmer_list: list[str]) -> str:
    return kmer_list[0] + ''.join([kmer[-1] for kmer in kmer_list[1:]])


if __name__ == '__main__':
    test_kmers = [
        'ACCGA',
        'CCGAA',
        'CGAAG',
        'GAAGC',
        'AAGCT'
    ]
    with open('chapter_3/inputs/string_from_path.txt', 'r') as in_fh:
        kmers = in_fh.read().strip().split('\n')
        print(string_from_path(kmers))
