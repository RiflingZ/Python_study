def fibonacci_counting(n):
    current = 0
    after = 1
    for i in range(n):
        current, after = after, current + after
    return current
    # 迭代


print(fibonacci_counting(36))
print(fibonacci_counting(5))
mass_of_earth = 5.9722 * 10**24  # kilograms
print(2**10)
mass_of_rabbit = 2  # 2 kilograms per rabbit

n = 1
while fibonacci_counting(n) * mass_of_rabbit < mass_of_earth:
    n += 1
print(n, fibonacci_counting(n))
