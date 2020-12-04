# 312 곱하기 혹은 더하기의 최댓값
import time
start = time.time()

num = input("문자열 입력: ")
total = int(num[0])

# 리스트의 숫자가 1,0이거나, total이 1,0 이면 더하고, 아니면 곱함
for i in range(1, len(num)):
    val = int(num[i])
    if val <= 1 or total <= 1:
        total += val
    else:
        total *= val

end = time.time()

print(total)
print(end - start)

