s = input().split('.')

for i in range(len(s)):
    x = list(s[i])
    n = len(x)
    if n % 2 != 0: #홀수일 경우에는 불가능
        print(-1)
        break
    else:
        if n == 2: # 2개인 경우
            x = 'BB'
        else: # 4개를 넘어가는 경우
            for j in range(0, 4 * (n//4)):
                x[j] = 'A'
            if n % 4 != 0: # 2개가 더 남은 경우
                x[-1] = 'B'
                x[-2] = 'B'
        s[i] = ''.join(x)
else:
    print('.'.join(s))
