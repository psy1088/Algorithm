# # 간단한 풀이
# from itertools import combinations
#
# data = []
# for _ in range(9):
#     data.append(int(input()))
#
# all_type = list(combinations(data, 7))
# for type in all_type:
#     if sum(type) == 100:
#         for i in sorted(type):
#             print(i)
#         break


# 다른풀이
def solution():
    diff = sum(data) - 100
    x, y = 0, 0
    for i in range(9):
        for j in range(9):
            if i != j:
                if data[i] + data[j] == diff:
                    x, y = data[i], data[j]
    data.remove(x)
    data.remove(y)

    return sorted(data)


data = []
for _ in range(9):
    data.append(int(input()))

for n in solution():
    print(n)


