for _ in range(int(input())):
    s = input()
    c = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            print(f'{c}{s[i-1]}', end='')
            c = 0
        c += 1
    if c != 0:
        print(f'{c}{s[-1]}', end='')
    print()