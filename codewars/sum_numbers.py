# Soma os valores de um array menos o maior e o menor valor

def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)


print(sum_array([6, 2, 1, 8, 10]))
print(sum_array(None))
print(sum_array([1, 1, 11, 2, 3]))
print(sum_array([3]))
