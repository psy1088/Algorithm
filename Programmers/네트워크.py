def dfs(i, computers, visited):
    for j in range(len(computers[i])):
        if i == j:
            continue

        if computers[i][j] == 1 and visited[j] == 0:
            visited[j] = 1
            dfs(j, computers, visited)


def solution(n, computers):
    visited = [0] * n
    res = 0

    for i in range(n):
        if visited[i] == 0:
            res += 1
            visited[i] = 1
            dfs(i, computers, visited)

    return res
