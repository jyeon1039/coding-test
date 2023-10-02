def solution(numbers):
    answer = []
    for n in numbers:
        if n%2 == 0: # 짝수 - 맨 뒤의 0을 1로 변환
            answer.append(n+1)
        else: # 홀수 - 뒤에서 0을 찾고, 그 위치를 1로 변환한 뒤, 0 뒤의 수를 0으로 변환
            n2 = '0' + bin(n)[2:] # 111 같은 경우에는 0을 찾을 수 없으므로 처음에 '0' 추가
            idx = n2.rfind('0')
            n2 = list(n2) # idx 문자를 변환하기 위해 list로 변경
            n2[idx] = '1'
            n2[idx+1] = '0'
            answer.append(int(''.join(n2), 2)) # int 함수 base=2 를 전달함을 통해 2진수라는 것을 명시
        
    return answer