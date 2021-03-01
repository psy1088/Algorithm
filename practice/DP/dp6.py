# p382 편집 거리
a = input()
b = input()


def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    d = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        d[i][0] = i
    for i in range(1, m + 1):
        d[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:  # 문자가 같다면, 왼쪽위의 수를 그대로 대입
                d[i][j] = d[i - 1][j - 1]
            else:  # 다르다면, 교체, 삭제, 삽입 중 제일 최소인 값 + 1 대입
                d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])
    return d[n][m]


print(edit_dist(a, b))
