import sys

n = int(sys.stdin.readline())
sg_cards = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
num_cards = map(int, sys.stdin.readline().split())
hashmap = {}

for x in sg_cards:
    if x in hashmap:
        hashmap[x] += 1
    else:
        hashmap[x] = 1

for x in num_cards:
    if x in hashmap:
        print(hashmap[x], end = ' ')
    else:
        print(0, end = ' ')
