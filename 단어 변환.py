min_cnt = 50

def check(now, word):
    diff = 0
    for i in range(len(word)):
        if now[i] != word[i]:
            diff += 1
    
    if diff == 1:
        return True
    else:
        return False


def dfs(now, target, words, visited, cnt):
    global min_cnt
    
    if now == target:
        min_cnt = min(min_cnt, cnt)
        return

    for i in range(len(words)):
        if visited[i] == 0 and check(now, words[i]):
            visited[i] = 1
            dfs(words[i], target, words, visited, cnt+1)
            visited[i] = 0


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [0] * len(words)
    dfs(begin, target, words, visited, 0)
    
    return min_cnt
