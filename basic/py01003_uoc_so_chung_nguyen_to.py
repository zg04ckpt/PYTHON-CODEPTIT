import math


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = math.gcd(a, b)
    s = sum([ord(i)-ord('0') for i in str(c)])
    print('YES' if is_prime(s) else 'NO')

