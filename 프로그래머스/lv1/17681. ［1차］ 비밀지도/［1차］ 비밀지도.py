def solution(n, arr1, arr2):
    answer = []

    map = [[0]*n for _ in range(n)]
    for i in range(n):
        # 지도 채우기
        for j in range(2):
            x = []
            if j == 0: # 지도1
                x = arr1[i]
            else: # 지도2
                x = arr2[i]
            
            tmp = [0]*n
            idx = n-1

            while x != 0:
                tmp[idx] = x %2
                x //= 2
                idx -= 1 
                
            for z in range(n):
                if tmp[z] == 1:
                    map[i][z] = 1

    for i in range(n):
        s = ""
        for j in range(n):
            if map[i][j] == 1:
                s += "#"
            else:
                s += " "
        answer.append(s)

    return answer