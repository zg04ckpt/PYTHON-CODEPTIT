for _ in range(int(input())):
    s = list(map(int,input()))
    # iterate from back
    for i in range(len(s)-1, 0, -1):
        if s[i] >= 5:
            s[i-1] += 1
        s[i] = 0
    print(''.join(map(str, s)))

