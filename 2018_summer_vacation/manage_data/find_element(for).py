def find_element(p, t):
    i = 0
    for e in p:
        if e == t:
            return i
        i = i + 1
    return -1


print(find_element([[1, 2, 3], 2, 3], 2))
print(find_element([[1, 2, 3], 2, 3], 1))
print(find_element([[1, 2, 3], 2, 3], [1, 2, 3]))
