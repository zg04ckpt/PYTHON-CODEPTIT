import math


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    n = int(input())
    k = 0
    for i in range(1, n):
        k += 1 if math.gcd(n, i) == 1 else 0
    print('YES' if is_prime(k) else 'NO')