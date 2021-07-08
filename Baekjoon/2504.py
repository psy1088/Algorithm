from collections import defaultdict
s = input()

cost = {')': 2, ']': 3}
pair = {')': '(', ']': '['}
cnt = defaultdict(int)
stack = []

val = ''
for i in s:
    if i in [')', ']']:
        cnt[pair[i]] -= 1 # 괄호 개수 하나 감소
        temp = 0
        while stack:
            val = stack.pop()
            if str(val).isdigit():
                temp += val
            else:
                break

        if val == pair[i]: # 괄호 쌍이 맞을 떄
            if temp == 0:
                stack.append(cost[i])
            else: # 괄호 내부에 숫자가 있다면 곱해줌
                stack.append(cost[i] * temp)
        else: # 쌍이 안맞을 경우 종료
            break

    else:
        stack.append(i)
        cnt[i] += 1

if cnt['('] == 0 and cnt['['] == 0:
    print(sum(stack))
else:
    print(0)
