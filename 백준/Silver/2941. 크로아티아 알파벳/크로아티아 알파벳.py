import sys

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = sys.stdin.readline().strip()

for i in arr:
    s = s.replace(i, '*')
print(len(s))