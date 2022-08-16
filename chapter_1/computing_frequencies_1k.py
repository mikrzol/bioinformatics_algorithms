from pattern_to_number_1l import pattern_to_number

def computing_frequencies(text: str, k: int) -> list[int]:
    frequency_array = [0] * (4**k)
    for i in range(0, len(text)-k+1):
        pattern = text[i:i+k]
        num_of_ptrn = pattern_to_number(pattern)
        frequency_array[num_of_ptrn] += 1
    return frequency_array

if __name__ == '__main__':
    with open('chapter_1/in_f.txt', 'r') as in_f:
        text = in_f.read().split('\n')
        arr = computing_frequencies(text=text[0], k=int(text[1]))
        print(' '.join([str(el) for el in arr]))