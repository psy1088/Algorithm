# 2021. 03.20 라인 코테 1번문제
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]

languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

score_arr = []
for x in range(len(table)):
    score = 0
    arr = table[x].split()
    for i in range(1, len(arr)):
        for j in range(len(languages)):
            if languages[j] == arr[i]:
                score += (6-i) * preference[j]

    score_arr.append((score, table[x][0], x))

score_arr.sort(key=lambda x: (-x[0], x[1]))
print(table[score_arr[0][2]].split()[0])




# 2021. 03.20 라인 코테 2번문제
def rule1(inp_str):
    if 8 <= len(inp_str) <= 15:
        return True
    else:
        return False


def rule2(inp_str):
    for s in inp_str:
        if ord('A') <= ord(s) <= ord('Z'):
            cnt[0] += 1
            continue
        if ord('a') <= ord(s) <= ord('z'):
            cnt[1] += 1
            continue
        if s.isdigit():
            cnt[2] += 1
            continue
        if s in spec:
            cnt[3] += 1

    if sum(cnt) == len(inp_str):
        return True
    else:
        return False


def rule3(inp_str):
    if cnt.count(0) < 2:
        return True
    else:
        return False


def rule4(inp_str):
    n = inp_str[0]
    con_cnt = 1
    for i in range(1, len(inp_str)):
        if con_cnt >= 4:
            return False
        if n == inp_str[i]:
            con_cnt += 1
        else:
            con_cnt = 1
        n = inp_str[i]
    if con_cnt >= 4:
        return False
    else:
        return True


def rule5(inp_str):
    set_arr = set(inp_str)
    for i in set_arr:
        if inp_str.count(i) >= 5:
            return False
    return True


def solution(inp_str):
    res = []
    if not rule1(inp_str):
        res.append(1)
    if not rule2(inp_str):
        res.append(2)
    if not rule3(inp_str):
        res.append(3)
    if not rule4(inp_str):
        res.append(4)
    if not rule5(inp_str):
        res.append(5)

    if res:
        res.sort()
    else:
        res.append(0)
    return res

inp_str = "AaTa+!12-3"
spec = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
cnt = [0, 0, 0, 0]
print(solution(inp_str))