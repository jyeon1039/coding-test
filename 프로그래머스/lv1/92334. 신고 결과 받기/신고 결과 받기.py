def solution(id_list, report, k):
    id_dic = {x : 0 for x in id_list} # 유저의 신고당한 횟수 저장
    report_dic = {x : [] for x in id_list} # 유저가 신고당한 ID 저장
    answer ={x : 0 for x in id_list} # 메일 전송 횟수 저장
    
    for x in report:
        a, b = x.split()
        if a not in report_dic[b]: # 처음 신고하는 경우
            report_dic[b].append(a)
            id_dic[b] += 1
    
    for user, cnt in id_dic.items():
        if cnt >= k:
            for x in report_dic[user]:
                answer[x] += 1
    
    return list(answer.values())