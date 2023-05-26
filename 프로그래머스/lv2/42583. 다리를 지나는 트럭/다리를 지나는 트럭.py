def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    sum_weight = 0
    
    while bridge:
        answer += 1
        sum_weight -= bridge.pop(0)

        if truck_weights:
            if truck_weights[0] + sum_weight <= weight:
                bridge.append(truck_weights.pop(0))
                sum_weight += bridge[-1]
            else:
                bridge.append(0)


    return answer