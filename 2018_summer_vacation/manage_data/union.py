def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


p = [1,2,3]
q = [2,4,6]
union(p,q)
print(p)
