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