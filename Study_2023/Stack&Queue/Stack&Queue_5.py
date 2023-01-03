def solution(bridge_length, weight, truck_weights):
    answer = 0

    Queue_bridge = []

    for _ in range(bridge_length):
        Queue_bridge.append(0)

    while Queue_bridge:

        answer += 1
        Queue_bridge.pop(0)

        if truck_weights:
            if sum(Queue_bridge) + truck_weights[0] <= weight:
                Queue_bridge.append(truck_weights.pop(0))
            else:
                Queue_bridge.append(0)

    return answer