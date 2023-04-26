# Given an n x n array, return the array elements arranged from outermost elements to the middle element,
# traveling clockwise.

def snail(snail_map):
    if not snail_map:
        return []
    elif len(snail_map) == 1:
        return snail_map[0]
    else:
        return snail_map[0] + snail([list(i) for i in zip(*snail_map[1:])][::-1])


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(snail(array))
