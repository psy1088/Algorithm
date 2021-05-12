from collections import defaultdict

def solution(tickets):
    
    # 탐색
    def dfs(start, res, N):
        if len(res) == N+1:
            return res
        
        for i, country in enumerate(dict[start]):
            next = dict[start].pop(i)
            
            temp_res = res[:]
            temp_res.append(next)
            
            answer = dfs(next, temp_res, N)
            if answer:
                return answer
            else:
                dict[start].insert(i, country)
        

    res = ["ICN"]
    dict = defaultdict(list)

    for a, b in tickets:
        dict[a].append(b)

    for d in dict: # 더 앞서는 알파벳을 먼저 방문하기 위해 정렬
        dict[d].sort()
        
    return dfs("ICN", res, len(tickets))
