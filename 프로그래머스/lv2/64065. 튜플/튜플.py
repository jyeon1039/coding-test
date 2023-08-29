def solution(s):
    answer = []
    s = s.lstrip("{").rstrip("}").split("},{")
    s.sort(key=len)
    
    for x in s:
        num = x.split(",")
        for n in num:
            n = int(n)
            if n not in answer:
                answer.append(n)
    
    return answer