# Recebe uma lista de numeros e retorna a soma dos negativos e a contagem dos positivos


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    else:
        return [len([x for x in arr if x > 0]), sum([x for x in arr if x < 0])]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))
