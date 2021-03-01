# p377 퇴사
N = int(input())
period, cost = [], []
for i in range(N):
    p, c = map(int, input().split())
    period.append(p)
    cost.append(c)

# N = 10  # 일하는 날짜
# period = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
# cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]

d = [0] * N
d[0] = cost[0]

for day in range(1, N):  # 2일부터 N일까지
    if day + period[day] <= N:  # 걸리는 시간을 고려했을 때 퇴사 날짜 이전이라면~
        d[day] = cost[day]
        for i in range(0, day):  # 가능한 상담 날짜를 고려하여, 0일부터 최대로 얻을 수 있는 금액과 더하여 저장
            if i + period[i] <= day:
                d[day] = max(d[day], d[i] + cost[day])

print(max(d))
