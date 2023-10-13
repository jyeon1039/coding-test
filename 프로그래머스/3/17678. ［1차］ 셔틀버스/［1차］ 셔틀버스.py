def solution(n, t, m, timetable):
    answer = ''
    timetable = [int(time[:2])*60+int(time[3:]) for time in timetable]
    timetable.sort()
    busTimetable = [9*60+t*i for i in range(n)]
    
    busCnt = 0 # 셔틀을 탄 사람들의 수
    for busTime in busTimetable:
        cnt = 0 # 이번 버스에 탄 사람들의 수
        while cnt < m and busCnt < len(timetable) and timetable[busCnt] <= busTime:
            cnt += 1
            busCnt += 1
        
        if cnt < m : # 버스에 자리가 남아있으면 이번 타임에 탑승
            answer = busTime
        else: # 버스에 탈 자리가 없으면 맨 마지막 크루보다 1분 전에 도착 (그래야 콘이 탑승 가능)
            answer = timetable[busCnt-1] - 1
        
    answer = str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
    return answer