# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.

def longest(s1, s2):
    return "".join(sorted(set(s1 + s2)))

print(longest("aretheyhere", "yestheyarehere"))
