# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.
table = []


def make_hashtable(nbuckets):
    for e in range(0, nbuckets):
        table.append([])
    return table


print(make_hashtable(3))
table[1].append(['udacity', ['http://udacity.com']])
print(table[1])
print(table[0])
