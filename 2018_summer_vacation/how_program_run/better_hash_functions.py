def hash_string(keyword,buckets):
    r = 0
    for char in keyword:
        r = (r + ord(char)) % buckets
    return r

print(hash_string('a',12))
# >>> 1

print(hash_string('b',12))
# >>> 2

print(hash_string('a',13))
# >>> 6

print(hash_string('au',12))
# >>> 10

print(hash_string('udacity',12))
# >>> 11
