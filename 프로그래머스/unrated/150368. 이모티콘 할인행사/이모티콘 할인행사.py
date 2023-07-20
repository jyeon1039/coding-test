from itertools import product

def solution(users, emoticons):
    answer = [0, 0] # 플러스 가입 수, 이모티콘 매출액
    discounts = [10, 20, 30, 40]
    
    for discount in product(discounts, repeat=7):
        total_pay, plus_num = 0, 0
        
        for rate, price in users:
            pay = 0
            for i, emoticon in enumerate(emoticons):
                if discount[i] >= rate: # 이모티콘의 할인율이 사용자가 원하는 할인율보다 높을 때
                    pay += emoticon * (100-discount[i]) // 100

            if pay >= price: # 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매 취소하고 이모티콘 플러스 가입
                plus_num += 1
            else:
                total_pay += pay
            
        if plus_num > answer[0]: # 이모티콘 플러스 가입자 수가 증가한 경우
            answer[0] = plus_num
            answer[1] = total_pay
        elif plus_num == answer[0] and total_pay > answer[1]: # 플러스 가입자 수는 같으면서 매출액이 증가한 경우
            answer[1] = total_pay
            
    return answer