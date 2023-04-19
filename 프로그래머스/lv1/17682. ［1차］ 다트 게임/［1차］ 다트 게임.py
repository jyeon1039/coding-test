def solution(dartResult):
    answer = 0
    bonus = {"S" : "**1", "D" : "**2", "T" : "**3"}
    dartList = []
    numList = []
    idx = 0
    for i, d in enumerate(dartResult, start = 0):
        if d in bonus: #보너스 체크
             dartList.append(bonus[d])
        
        elif d == "*" and i-2 == 0: #스타상 첫번째일 때
            print(i)
            dartList.append("*2")         
    
        elif d == "*": #스타상 첫번째가 아닐 때
            print(i)
            dartList.append("*2")
            print(dartList)
            dartList.insert(len(dartList)-4,"*2")
            print(dartList)
               
        elif d == "#": #아차상일 때
            dartList.append("*(-1)")
            
        elif  d.isdigit() and i != 0 and dartList[-1].isdigit() == False: #숫자이고 10이 아닐 때
            dartList.append("+")
            dartList.append(d)
                
        else:
            dartList.append(d)

    result = ''.join(map(str, dartList))
    
    print(dartList)
    
    return eval(result)