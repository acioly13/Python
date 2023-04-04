# Contador de ovelha True = 1, False = 0

def count_sheeps(arrayOfSheeps):
    count = 0
    for i in arrayOfSheeps:
        if i:
            count += 1
    return count


print(count_sheeps(
    [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True,
     True, True, False, False, True, True]))
