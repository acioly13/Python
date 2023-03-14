# Distância Hamming

def hamming_distance(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 != len_s2:
        raise ValueError("Sequencias de Tamanhos Diferentes")
    dist = 0
    for i in range(len_s1):
        if s1[i] != s2[i]:
            dist += 1
    return dist


print(hamming_distance("marcus", "marcos"))
print(hamming_distance("0101", "1110"))
