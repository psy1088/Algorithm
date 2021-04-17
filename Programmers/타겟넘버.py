def dfs(numbers, target, index, result):
    global cnt
    if index >= len(numbers):
        if result == target:
            cnt += 1
        return

    for d in [-1, 1]:
        dfs(numbers, target, index+1, result + numbers[index] * d)


cnt = 0
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt
