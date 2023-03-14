def convertToDay(day):
    yy, mm, dd = map(int, day.split('.'))
    return yy*12*28 + mm*28 + dd 
    
def solution(today, terms, privacies):
    answer = []
    terms_day = {}
    idx = 1
    
    for term in terms:
        t, m = term.split()
        terms_day[t] = int(m)*28
    
    today = convertToDay(today)
    
    for privacy in privacies:
        day, t = privacy.split()
        day = convertToDay(day)
        if today >= day + terms_day[t]:
            answer.append(idx)
            
        idx += 1
        
    return answer