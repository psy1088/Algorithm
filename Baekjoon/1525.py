def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        now_str = q.popleft() # 현재 문자열
        if now_str == '123456780':
            return visited[now_str]

        i = now_str.index('0') # 0의 인덱스 찾기
        now_r, now_c = i // 3, i % 3 # 문자열을 2차원배열로 생각했을 때의 행과 열
        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if 0 <= next_r < 3 and 0 <= next_c < 3:
                next_i = next_r * 3 + next_c
                next_str = list(now_str)
                next_str[i], next_str[next_i] = next_str[next_i], next_str[i]
                next_str = ''.join(next_str)

                if next_str not in visited:
                    q.append(next_str)
                    visited[next_str] = visited[now_str] + 1
    return -1


from collections import deque
import sys
input = sys.stdin.readline

data = ''
for _ in range(3):
    line = list(input().split())
    data += ''.join(line)

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

visited = {}
print(bfs(data))
