def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deli_n = 0
    pick_n = 0
    for i in range(n-1, -1, -1):
        deli_n -= deliveries[i]
        pick_n -= pickups[i]
        
        while deli_n < 0 or pick_n < 0:
            deli_n += cap
            pick_n += cap
            answer += (i+1)*2
    
    return answer