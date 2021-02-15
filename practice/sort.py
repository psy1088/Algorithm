# # p178 위에서 아래로
# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(int(input()))
#
# arr.sort(reverse=True)
#
# for i in arr:
#     print(i, end=' ')


# # p180 성적이 낮은 순서로 학생 출력하기
# N = int(input())
#
# student = []
# for i in range(N):
#     data = input().split()
#     student.append((data[0], int(data[1])))
#
# student.sort(key=lambda x: x[1])
# student = sorted(student, key=lambda x: x[1])
#
# for s in student:
#     print(s[0], end=' ')


# p182 두 배열의 원소 교체
N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순, b는 내림차순 정렬
a.sort()
b.sort(reverse=True)
for i in range(K):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

result = sum(a)
print(result)
