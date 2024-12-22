import re
# use regex to find any char except '4' and '7'
for _ in range(int(input())):
    print('NO' if re.search(r'[^47]', input()) else 'YES')
