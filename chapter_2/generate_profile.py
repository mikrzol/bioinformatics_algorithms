def generate_profile(motifs: list[str]):
    adenines = [[motif[i] for motif in motifs].count('A')/len(motifs) for i in range(len(motifs[0]))]
    cytosines = [[motif[i] for motif in motifs].count('C')/len(motifs) for i in range(len(motifs[0]))]
    guanines = [[motif[i] for motif in motifs].count('G')/len(motifs) for i in range(len(motifs[0]))]
    thymines = [[motif[i] for motif in motifs].count('T')/len(motifs) for i in range(len(motifs[0]))]

    return [adenines, cytosines, guanines, thymines]

    


if __name__ == '__main__':
    test_motifs = [
        'TCGGGGGTTTTT',
        'CCGGTGACTTAC',
        'ACGGGGATTTTC',
        'TTGGGGACTTTT',
        'AAGGGGACTTCC',
        'TTGGGGACTTCC',
        'TCGGGGATTCAT',
        'TCGGGGATTCCT',
        'TAGGGGAACTAC',
        'TCGGGTATAACC'
    ]

    print(generate_profile(motifs=test_motifs))