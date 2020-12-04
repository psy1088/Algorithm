# 314 만들 수 없는 금액의 최솟값
n = int(input())
unit = list(map(int, input().split()))

unit.sort()
min_val = 1

# 오름차순 정렬 된 리스트에서 차례로 더해갈 때, 그 다음 인덱스 값보다 작다면 그 다음 값은 만들 수 없다
for i in unit:
    if min_val < i:
        break
    min_val += i

print(min_val)
