for _ in range(int(input())):
    s = input()
    for i in range(0, len(s), 2):
        for _ in range(int(s[i+1])):
            print(s[i], end='')
    print()