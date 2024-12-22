for _ in range(int(input())):
    n, x, m = map(float, input().split())
    c = 0
    while n < m:
        n += n * (x/100)
        c += 1
    print(c)

