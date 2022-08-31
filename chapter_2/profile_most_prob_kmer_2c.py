import numpy as np

def kmer_probability(kmer: str, profile_dict: dict) -> float:
    return np.prod([profile_dict[nucl][i] for i, nucl in enumerate(kmer)])


def profile_most_probable_kmer(seq: str, k: int, profile_matrix_str: list[str] = [], profile_matrix_list: list[list[float]] = []) -> str:
    if profile_matrix_str:
        profile_dict = dict(zip(['A', 'C', 'G', 'T'], 
            [[float(x) for x in profile_matrix_str[i].split(' ')] for i in range(0, len(profile_matrix_str))]
        ))
        ''' THE ABOVE DOES THIS IN ONE LINE:
        profile_dict = {
            'A': [float(x) for x in profile_matrix[0].split(' ')],
            'C': [float(x) for x in profile_matrix[1].split(' ')],
            'G': [float(x) for x in profile_matrix[2].split(' ')],
            'T': [float(x) for x in profile_matrix[3].split(' ')]
        }
        '''
    else:
        profile_dict = dict(zip(['A', 'C', 'G', 'T'], profile_matrix_list))

    most_probable_kmer = seq[0:k]
    most_probable_kmer_prob = kmer_probability(most_probable_kmer, profile_dict)
    for i in range(0, len(seq) - k + 1):
        if kmer_probability(seq[i:i+k], profile_dict) > most_probable_kmer_prob:
            most_probable_kmer_prob = kmer_probability(seq[i:i+k], profile_dict)
            most_probable_kmer = seq[i:i+k]
    
    return most_probable_kmer


if __name__ == '__main__':
    with open('chapter_2/inputs/profile_most_probable_kmer.txt', 'r') as in_fh:
        text = in_fh.read().strip().split('\n')
        seq = text[0].strip()
        k = int(text[1].strip())
        profile_matrix_str = text[2:]
        print(profile_most_probable_kmer(seq, k, profile_matrix_str))

