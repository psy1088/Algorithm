# p322 문자열 재정렬
S = input()
arr_str = []
res = 0

for i in S:
    if i.isalpha():
        arr_str.append(i)
    else:
        res += int(i)
arr_str.sort()

if res != 0:
    arr_str.append(str(res))

print(''.join(arr_str))


## 2
# S = input()
#
# char = []
# num_sum = 0
#
# char_min = ord('A')
# char_max = ord('Z')
#
# for i in S:
#     if char_min <= ord(i) <= char_max:
#         char.append(i)
#     else:
#         num_sum += int(i)
#
# char.sort()
#
# for i in char:
#     print(i, end='')
# print(num_sum)
