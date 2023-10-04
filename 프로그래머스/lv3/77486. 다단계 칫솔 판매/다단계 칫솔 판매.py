def bfs(seller, amount, tree, idx):
    global answer
    if seller == '-':
        return
    
    a = int(amount*0.1)
    answer[idx[seller]] += amount - a
    
    if a >= 1: # 1원 미만인 경우에는 분배 X
        bfs(tree[seller], a, tree, idx) # 10% 배분
    
def solution(enroll, referral, seller, amount):
    global answer
    answer = [0]*len(enroll)
    tree = {}
    idx = {}

    for i in range(len(enroll)):
        tree[enroll[i]] = referral[i]
        idx[enroll[i]] = i
        
    for i in range(len(seller)):
        s = seller[i]
        a = amount[i]*100
        bfs(s, a, tree, idx)
            
    return answer