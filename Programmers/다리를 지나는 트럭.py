from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque()
    cnt_truck = len(truck_weights)
    
    truck_index = 0
    while truck_index < cnt_truck:
        if len(q) == bridge_length: # 도로가 꽉 차있다면, 맨 앞 제거
            q.popleft()
        if sum(q) + truck_weights[truck_index] > weight: # 다음 트럭에 도로가 견딜 수 없다면 0 삽입
            now_truck = 0
        else:
            now_truck = truck_weights[truck_index]
            truck_index += 1
        
        q.append(now_truck)
        time += 1
    time += bridge_length # 마지막 트럭이 통과하는 시간 더해줌
    
    return time
