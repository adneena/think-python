def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.
    Simple version using a for loop.
    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


t = [1, 2, 3]
print(has_duplicates(t))
t.append(1)
print(has_duplicates(t))
