# p349 연산자 끼워넣기
n = 6  # 숫자의 개수
a = [1, 2, 3, 4, 5, 6]  # n개의 숫자
add, sub, mul, div = 2, 1, 1, 1  # 덧셈, 뺄셈, 곱셈, 나눗셈
min_val, max_val = 1e9, -1e9


def dfs(i, now):
    global add, sub, mul, div, min_val, max_val

    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + a[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - a[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * a[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / a[i]))
            div += 1


dfs(1, a[0])
print(max_val)
print(min_val)