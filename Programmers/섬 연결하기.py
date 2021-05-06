def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]
        
    
def union_parent(parent, x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
        

def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n)]
    answer = 0
    edge_cnt = 0
    
    for a, b, cost in costs:
        if edge_cnt == n-1:
            break
            
        x, y = find_parent(parent, a), find_parent(parent, b)
        if x != y: # 부모가 같다면, 싸이클 형성
            union_parent(parent, x, y)
            answer += cost
            edge_cnt += 1
            
    return answer
