# from collections import deque
#
# alpha = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
#
# data = input()
# trans_data = deque()
# for i in range(len(data)):
#     trans_data.append(alpha[ord(data[i]) - ord('A')])
#
# while len(trans_data) > 1:
#     for _ in range(len(trans_data) // 2):
#         a = trans_data.popleft()
#         b = trans_data.popleft()
#         trans_data.append((a+b) % 10)
#     trans_data.append(trans_data.popleft())
#
# if trans_data.popleft() % 2 == 0:
#     print("You're the winner?")
# else:
#     print("I'm a winner!")


alpha = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
data = input()
res = 0
ord_A = ord('A')
for d in data:
    res += alpha[ord(d) - ord_A]

res %= 2
if res == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")
