def solution(arr):
     for i in range(1, len(arr)):
        arr[i][0] += arr[i-1][0] # 줄의 맨 첫째값
        arr[i][-1] += arr[i-1][-1] # 줄의 맨 끝값
        
        for j in range(1, len(arr[i])-1):
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
    
     return max(arr[-1])
