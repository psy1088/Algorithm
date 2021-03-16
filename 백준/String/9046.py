import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dic = {}
    data = input().rstrip()  # 맨뒤 개행문자 제거해서 입력
    for i in data:
        if i.isalpha():
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

    dic = sorted(dic.items(), key=lambda x: -x[1])
    s1 = dic.pop(0)
    s2 = dic.pop(0) if dic else (0, 0)
    if s1[1] == s2[1]:
        print('?')
    else:  # 아니면, 제일 큰 값 출력
        print(s1[0])
