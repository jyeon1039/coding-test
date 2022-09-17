#최소 2가지 이상의 단품 메뉴
#2명 이상의 손님으로부터 주문된 단품메뉴 조합
from itertools import combinations

def solution(orders, course):
    answer = []
    dic = {}
    maxValue = {}
    
    for order in orders:
        order = list(order)
        order.sort()
        for count in course:
            combination = list(combinations(order, count))
            for x in combination:
                x = ''.join(x)
                if x in dic:
                    dic[x] += 1
                else:
                    dic[x] = 1
                
                if count not in maxValue:
                    maxValue[count] = 1
                else:
                    if maxValue[count] < dic[x]:
                        maxValue[count] = dic[x]

    for x in dic:
        if dic[x] == maxValue[len(x)]:
            if maxValue[len(x)] != 1:
                answer.append(x)

    answer.sort()
    
    return answer