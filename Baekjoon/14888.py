# from itertools import permutations
# import sys
# input = sys.stdin.readline
#
# N = int(input()) # 숫자의 개수
# A = list(map(int, input().split())) # 숫자 집합
# oper = list(map(int, input().split())) # 연산자 집합
#
# # 덧셈:0, 뺼셈:1, 곱셈:2, 나눗셈:3
# operator = []
# for i in range(4):
#     for j in range(oper[i]):
#         operator.append(i)
#
# max_res = -1e9
# min_res = 1e9
# for case in set(permutations(operator, N-1)):
#     res = A[0]
#
#     for x in range(N-1):
#         if case[x] == 0: # 덧셈
#             res += A[x+1]
#         elif case[x] == 1: # 뺄셈
#             res -= A[x+1]
#         elif case[x] == 2: # 곱셈
#             res *= A[x+1]
#         elif case[x] == 3:  # 나눗셈
#             temp = abs(res) // A[x+1] # 음수일 경우도 양수로 바꿔서 나눗셈한다음 부호 취해줌
#             res = temp if res >= 0 else -temp
#
#     min_res = min(min_res, res)
#     max_res = max(max_res, res)
#
# print(max_res)
# print(min_res)

import sys
input = sys.stdin.readline


def dfs(cnt, result):
    global min_val, max_val

    if cnt == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    if operator[0]:  # 덧셈
        operator[0] -= 1
        dfs(cnt+1, result + A[cnt])
        operator[0] += 1
    if operator[1]: # 뺄셈
        operator[1] -= 1
        dfs(cnt+1, result - A[cnt])
        operator[1] += 1
    if operator[2]: # 곱셈
        operator[2] -= 1
        dfs(cnt+1, result * A[cnt])
        operator[2] += 1
    if operator[3]: # 나눗셈
        operator[3] -= 1
        dfs(cnt+1, int(result / A[cnt]))
        operator[3] += 1



N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_val, min_val = -1e9, 1e9
dfs(1, A[0])
print(max_val)
print(min_val)
