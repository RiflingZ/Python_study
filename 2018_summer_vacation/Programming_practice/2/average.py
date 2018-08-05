# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(p):
    if p == []:
        return True
    if len(p) != len(p[0]):
        return False
    for num in range(len(p)):
        row = []
        col = []
        for n in range(len(p)):
            row.append(p[num][n])
            col.append(p[n][num])
        print("round %s : %s, %s" % (num, row, col))
        if row != col:
            return False
    return True


print(symmetric([]))
print(symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]]))
print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish", "fish", "cat"]]))
print(symmetric([[1, 2],
                [2, 1]]))
print(symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))
print(symmetric([[1, 2, 3],
                 [2, 3, 1]]))
