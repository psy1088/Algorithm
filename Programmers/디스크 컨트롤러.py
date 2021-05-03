from collections import deque
import heapq

def solution(jobs):
    jobs.sort(key=lambda x:(x[0], x[1])) # 요청시간을 기준으로 정렬
    jobs = deque(jobs)
    
    executable = []
    cur_t = 0 # 현재 시각
    total_t = 0 # 총 걸린시간
    task = 0 # 처리한 작업 수
    len_jobs = len(jobs)
    
    while task < len_jobs:
        # 현 시점(start)에서 처리가능한 모든 작업 저장
        while jobs:
            req_t, elapse_t = jobs.popleft()
            if req_t <= cur_t: # 처리가능하면 힙에 저장 (소요시간 기준으로 뽑아야하므로 (소요시간, 요청시간)으로 저장
                heapq.heappush(executable, (elapse_t, req_t))
            else:
                jobs.appendleft((req_t, elapse_t))
                break

        # 실행 가능한 게 있으면, 하나 실행
        if executable:
            elapse_t, req_t = heapq.heappop(executable)
            cur_t += elapse_t
            total_t += (cur_t - req_t)
            task += 1

        # 실행 가능한 게 없으면, 현재 시각 변경
        else:
            cur_t = jobs[0][0]

    return total_t // task
