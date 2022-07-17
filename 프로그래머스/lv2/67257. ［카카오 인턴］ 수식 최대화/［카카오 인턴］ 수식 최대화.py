from copy import deepcopy

# 우선순위에 따른 상금 계산
def calculate(operator, expression):
    arr = deepcopy(expression)
    
    for op in operator:
        if len(arr) == 1: # 하나만 남았다면 끝났으니까 break
            break
        idx = 1
        
        while True:
            if arr[idx] == op:
                a = int(arr[idx-1])
                b = int(arr[idx+1])

                if op == '*':
                    arr[idx-1] = a * b
                elif op == '+':
                    arr[idx-1] = a + b
                elif op == '-':
                    arr[idx-1] = a - b
                
                arr.pop(idx+1)
                arr.pop(idx)
                idx -= 1 # 현재 위치를 다시 고려하기 위하여
            idx += 1
            
            if idx >= len(arr)-1:
                break
    
    if arr[0] < 0:
        return -arr[0]
    else:
        return arr[0] 
                
def solution(expression):
    answer = 0
    arr = []
    operator = [['*','+','-'], ['*','-','+'], ['+','*','-'],
               ['+','-','*'], ['-','*','+'], ['-','+','*']]
    tmp = ''
    for x in expression:
        if '0' <= x <= '9':
            tmp += x
        else:
            arr.append(tmp)
            arr.append(x)
            tmp = ''
    arr.append(tmp)
    
    for op in operator:
        res = calculate(op, arr)
        
        if answer < res:
            answer = res
    
    return answer