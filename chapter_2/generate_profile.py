def generate_profile(motifs: list[str], laplace_succession: bool = False) -> list[list[float]]:
    # fill in motifs with Ns to make their lengths uniform
    max_length = max(map(len, motifs))
    for i in range(len(motifs)):
        if len(motifs[i]) < max_length:
            motifs[i] += 'N' * (max_length - len(motifs[i]))

    if laplace_succession:
        # get counts
        adenines = [[motif[i] for motif in motifs].count('A') + 1  for i in range(len(motifs[0]))]
        cytosines = [[motif[i] for motif in motifs].count('C') + 1 for i in range(len(motifs[0]))]
        guanines = [[motif[i] for motif in motifs].count('G') + 1  for i in range(len(motifs[0]))]
        thymines = [[motif[i] for motif in motifs].count('T') + 1  for i in range(len(motifs[0]))]

        # change them to probabilities
        for i in range(max_length):
            total_nucls = sum([nucl[i] for nucl in [adenines, cytosines, guanines, thymines]])
            adenines[i] *= 1 / total_nucls
            cytosines[i] *= 1 / total_nucls
            guanines[i] *= 1 / total_nucls
            thymines[i] *= 1 / total_nucls
        
    else:
        adenines = [[motif[i] for motif in motifs].count('A')/len(motifs) for i in range(len(motifs[0]))]
        cytosines = [[motif[i] for motif in motifs].count('C')/len(motifs) for i in range(len(motifs[0]))]
        guanines = [[motif[i] for motif in motifs].count('G')/len(motifs) for i in range(len(motifs[0]))]
        thymines = [[motif[i] for motif in motifs].count('T')/len(motifs) for i in range(len(motifs[0]))]

    return [adenines, cytosines, guanines, thymines]

    


if __name__ == '__main__':
    test_motifs = [
        'TCGGGGGTTTTTA',
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
    test_motifs_2 = [
        'TAACA',
        'GTCT',
        'ACTA',
        'AGGT'
    ]

    print(generate_profile(motifs=test_motifs_2, laplace_succession=True))