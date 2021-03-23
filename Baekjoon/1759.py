from itertools import combinations

L, C = map(int, input().split())  # L=암호 길이, C=주어진 문자 개수
data = input().split()

data.sort()
all_type = list(combinations(data, L))

for type in all_type:
    c_cnt, v_cnt = 0, 0
    for i in type:
        if i in "aeiou":  # 모음 개수
            c_cnt += 1
        else:  # 자음 개수
            v_cnt += 1

    if c_cnt >= 1 and v_cnt >= 2:
        print(''.join(type))
