import re

# generate a array of valid number by concatenate s and reversed s
# exp: 204 -> 204 + 402 = 204402
li = []
for i in range(2, 10**3, 2):
    s = str(i)
    if not re.search(r'[^02468]', s):
        li.append(int(s + ''.join(s[::-1])))

for _ in range(int(input())):
    n = int(input())
    i = 0
    while i < len(li) and li[i] < n:
        print(li[i], end=' ')
        i += 1
    print()
