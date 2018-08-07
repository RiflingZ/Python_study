def list_mean(p):
    sum = 0
    for e in p:
        sum = sum + e
    return sum / float(len(p))


print(list_mean([1, 2, 3, 4]))
print(list_mean([1, 3, 4, 5, 2]))
print(list_mean([2]))
