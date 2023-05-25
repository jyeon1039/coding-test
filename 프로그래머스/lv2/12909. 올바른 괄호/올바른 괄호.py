def solution(s):
    answer = True
    stack = []
    
    for x in s:
        if x == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                e = stack.pop()
                if e != '(':
                    return False
    
    if len(stack) == 0:
        return True
    else:
        return False