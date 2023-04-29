s = input()

s = s.replace('XXXX', 'AAAA')
s = s.replace('XX', 'BB')

if s.count('X') != 0:
    print(-1)
else:
    print(s)