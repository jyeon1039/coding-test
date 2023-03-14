def convertToDay(day):
    yy, mm, dd = map(int, day.split('.'))
    return yy*12*28 + mm*28 + dd 
    
def solution(today, terms, privacies):
    answer = []
    terms_day = {}
    idx = 1
    
    # 각 약관의 유효기간 저장
    for term in terms:
        t, m = term.split()
        terms_day[t] = int(m)*28 # 일수 기준으로 저장하기 위해 28 곱함
    
    today = convertToDay(today)
    
    for privacy in privacies:
        day, t = privacy.split()
        day = convertToDay(day)
        if today >= day + terms_day[t]: # 유효기간이 지났을 경우
            answer.append(idx)
            
        idx += 1
        
    return answer