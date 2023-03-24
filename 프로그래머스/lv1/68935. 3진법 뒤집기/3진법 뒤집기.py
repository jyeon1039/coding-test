def convertToReverseTernary(n):
    result = ""
    while n != 0:
        x = n % 3 #나머지
        n //= 3
        result += str(x)
    return int(result)
     
def convertToDecimal(n):
    result = 0
    x = 0
    while n != 0:
        result += (3**x) * (n%10)
        x += 1
        n //= 10
    return result
        
def solution(n):
    n = convertToReverseTernary(n)
    return convertToDecimal(n)