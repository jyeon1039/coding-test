import sys

n = int(sys.stdin.readline())
users = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    users.append((age, name))

users.sort(key=lambda x:int(x[0]))

for (age, name) in users:
    print(age, name)
        
