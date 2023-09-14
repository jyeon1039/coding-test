def transfer(n, k):
    result = ""
    while(n != 0):
        result = str(n%k) + result
        n //= k
        
    return result

def isPrime(n):
    # 소수인지 확인
    for x in range(2, int(n**0.5 + 1)):
        if n % x == 0:
            return 0
    else:
        return 1
    
def solution(n, k):
    answer = 0
    n = transfer(n, k)
    left = 0
    right = 1
    
    # 0을 기준으로 잘라서 소수인지 확인
    for x in n.split('0'):
        if x == '1' or x =='':
            continue
        
        answer += isPrime(int(x))
        
    return answer