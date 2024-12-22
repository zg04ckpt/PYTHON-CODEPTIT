import re

# using regex to find all '4' and '7'. 
# Result is an array => need only check len of array
c = len(re.findall(r'[4|7]', input()))
print('YES' if c == 4 or c == 7 else 'NO')
