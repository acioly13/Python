# Recebe uma lista e soma os 2 menores valores dessa lista

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


print(sum_two_smallest_numbers([9, 10, 2, 5, 4]))
