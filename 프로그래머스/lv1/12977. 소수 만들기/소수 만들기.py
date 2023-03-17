from itertools import combinations
import math

# 소수인지를 판별하는 함수
def isPrimeNumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
        	return False
    return True	 

def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3)) # 조합 구하기

    for x in combi:
        if isPrimeNumber(sum(x)):
            answer += 1
                    
    return answer