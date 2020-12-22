# p333 치킨 배달
from itertools import combinations

### input값 입력
N, M = list(map(int, input().split()))  # 맵의 크기, 폐업 시키지 않을 치킨집 수
data, home, chicken = [], [], []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:  # 집
            home.append((i, j))
        elif data[j] == 2:  # 치킨집
            chicken.append((i, j))


### 치킨 거리 최솟값 구하기
choice = list(combinations(chicken, M))  # 치킨집 리스트 원소 중 M개를 뽑음

min_total = 1e9  # 도시의 치킨 거리 최솟값
total = 0  # 도시의 치킨 거리
for cho in choice:
    total = 0
    for hr, hc in home:
        min_dis = N + N  # home에서 선택된 chicken까지의 최소거리
        for i in range(len(cho)):
            r = abs(cho[i][0] - hr)  # 절댓값
            c = abs(cho[i][1] - hc)
            min_dis = min(min_dis, r + c)
        total += min_dis
    min_total = min(min_total, total)

print(min_total)