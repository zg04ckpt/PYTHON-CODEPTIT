for _ in range(int(input())):
    s = input()
    e = ''.join(sorted(s)) # e = sorted s 
    print('YES' if s == e else 'NO')