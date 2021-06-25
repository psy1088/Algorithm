result = []

def trans_arr(arr, r1, c1, r2, c2):
    edge = [arr[r2-1][c2-1]]
    
    for c in range(c2-2, c1-2, -1):
        edge.append(arr[r2-1][c])
        arr[r2-1][c] = edge[-2]
        
    for r in range(r2-2, r1-2, -1):
        edge.append(arr[r][c1-1])
        arr[r][c1-1] = edge[-2]
        
    for c in range(c1, c2):
        edge.append(arr[r1-1][c])
        arr[r1-1][c] = edge[-2]
        
    for r in range(r1, r2):
        edge.append(arr[r][c2-1])
        arr[r][c2-1] = edge[-2]
    
    result.append(min(edge))
    return arr
    

def solution(rows, columns, queries):
    arr = [[(j*columns)+i+1 for i in range(columns)] for j in range(rows)]
    
    for r1, c1, r2, c2 in queries:
        arr = trans_arr(arr, r1, c1, r2, c2) # 리스트 회전하고 최솟값 반환
        
    return result
