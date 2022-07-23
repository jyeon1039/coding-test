def solution(s):
    answer = []
    
    s = s.replace("{", " ").replace("},", " ").replace("}}", "")
    tmp = s.split()
    arr = []
    for x in tmp:
        arr.append(list(map(int, x.split(","))))
        
    arr.sort(key=len)
    for x in arr:
        for y in x:
            if y not in answer:
                answer.append(y)
    
    return answer