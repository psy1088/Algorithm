from itertools import combinations

def find_pair():
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            left = stack.pop()
            pair.append((left, i))


def remove_pair(case):
    _remove = []
    for x, y in case: # 괄호쌍의 모든 좌표 저장
        _remove.append(x)
        _remove.append(y)
    _remove.sort()

    temp = ''
    k, now = 0, 0
    for j in range(len(s)):
        if j == _remove[k]:
            k += 1
            if k == i*2: # 마지막 괄호가 끝났다면 중단
                now = j
                break
        else:
            temp += s[j]

    if len(s) > now+1: # 마지막 괄호가 끝난 지점이 문자열의 마지막이 아니라면, 나머지를 추가해줌
        temp += s[now+1:]

    result.append(temp)


s = input()

pair = [] # 괄호 쌍의 좌표 저장
result = []

find_pair()
for i in range(1, len(pair)+1): # 제거할 괄호쌍의 수
    for case in combinations(pair, i): # i개의 괄호쌍을 제거하는 경우
        remove_pair(case)

result = list(set(result))
print('\n'.join(sorted(result)))
