r, c = map(int, input().split())  # r=세로길이, c=가로길이

if r == 1:  # 세로가 1칸이면, 이동불가
    print(1)
elif r == 2:  # 세로가 2칸이면, 2 3번 방법으로만 이동 가능
    print(min(4, 1+(c-1)//2))
else:  # 세로가 3칸 이상일때,
    if 7 <= c:  # 가로가 7칸 이상일때만 4번 이상 이동가능
        print(c - 2)
    else:
        print(min(4, c))
