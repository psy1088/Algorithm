attendance = [0 for _ in range(30)]

for _ in range(28):
    n = int(input())
    attendance[n-1] = 1

# 1번 방법 : filter 사용
result = list(filter(lambda x: attendance[x] == 0, range(30)))

# 2번 방법 : enumerate 사용 => 인덱스와 값을 튜플형태로 출력
result = [i for i in enumerate(attendance) if i[1] == 0]

# 3번 방법 : 그냥 하나씩 쭉 확인하기
# for i in range(30):
#     if attendance[i] == 0:
#         print(i+1)

#
# for i in result:
#     print(i+1)
