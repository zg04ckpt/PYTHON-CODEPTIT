for _ in range(int(input())):
    s = input()
    print('YES' if s[0] == s[-2] and s[1] == s[-1] else 'NO')
