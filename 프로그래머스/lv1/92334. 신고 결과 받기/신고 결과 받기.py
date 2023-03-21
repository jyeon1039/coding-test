def solution(id_list, report, k):
    id_dic = dict(zip(id_list, [0 for i in id_list])) # 유저의 신고당한 횟수 저장
    report_dic = dict(zip(id_list, [[] for i in id_list])) # 유저가 신고당한 ID 저장
    mail_dic = dict(zip(id_list, [0 for i in id_list])) # 메일 전송 횟수 저장
    for x in report:
        a, b = x.split()
        if a not in report_dic[b]: # 처음 신고하는 경우
            report_dic[b].append(a)
            id_dic[b] += 1
    
    for user, cnt in id_dic.items():
        if cnt >= k:
            for x in report_dic[user]:
                mail_dic[x] += 1
    
    return list(mail_dic.values())