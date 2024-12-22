a, k, n = map(int, input().split())

has = False
# handle with sum of a + b, optimize for to alway mod k = 0
for s in range(k, n+1, k):
    if s > a:
        has = True
        print(s-a, end=' ')
if not has:
    print(-1)