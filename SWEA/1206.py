T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())  # 아파트 수
    building = list(map(int, input().split()))

    total = 0  # 총 세대 수
    for i in range(2, n - 1):
        good_view = building[i]
        flag = True
        for j in range(i - 2, i + 3):  # 현재 빌딩에서 좌우 2칸씩 검사
            if i != j:  # 자기 자신 제외
                if building[i] - building[j] <= 0:
                    flag = False
                    break
                good_view = min(good_view, building[i] - building[j])  # 좌우2칸 빌딩 중에 제일 적은 차이값을 저장

        if flag:
            total += good_view

    print("#", end='')
    print(test_case, total)
