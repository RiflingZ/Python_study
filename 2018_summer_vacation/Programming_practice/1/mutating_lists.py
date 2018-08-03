def proc4(p):
    q = []
    while p:#p is not empty
        q.append(p.pop())#reverse
    while q:#q is not empty
        p.append(q.pop())#agin


p = [1,2,3]
proc4(p)
print(p)