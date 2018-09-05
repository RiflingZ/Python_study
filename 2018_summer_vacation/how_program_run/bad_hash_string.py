def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets
