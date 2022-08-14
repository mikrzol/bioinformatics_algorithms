# PATTERN COUNT
def pattern_count(text: str, pattern: str) -> int:
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

if __name__ == '__main__':
    txt1 = 'ACAACTATGCATACTATCGGGAACTATCCT'
    ptrn1 = 'ACTAT'

    txt2 = 'CGATATATCCATAG'
    ptrn2 = 'ATA'

    print(pattern_count(txt2, ptrn2))