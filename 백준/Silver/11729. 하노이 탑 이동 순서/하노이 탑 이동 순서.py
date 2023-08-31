def hanoi(n, start, to, via):
    if n==1:
        print(start, to) # 종료조건: n이 1일 때는 1을 목적지로 옮긴다
    else:
        hanoi(n-1, start, via, to) # n-1개의 원판을 옮기기 위해서 n-1개의 원판을 경우지로 옮긴다
        print(start, to) # n원판을 목적지로 옮긴다
        hanoi(n-1, via, to, start) # n-1개의 원판을 목적지로 옮긴다

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)