def hash_string(keyword, buckets):
    h = 0
    for char in keyword:
        h = (h + ord(char)) % buckets
    return h


print(hash_string('a', 12))
# >>> 1

print(hash_string('b', 12))
# >>> 2

print(hash_string('a', 13))
# >>> 6

print(hash_string('au', 12))
# >>> 10

print(hash_string('udacity', 12))
# >>> 11

b = ord('u') + 1
print(b % 12)
print(hash_string('Francis', 5))
