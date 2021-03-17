# 이건 시간초과,,,,
# def Oct_to_binary(n):
#     if n <= 1:
#         return str(n)
#     answer = ''
#     while True:
#         if n % 2 == 0:
#             answer += '0'
#         else:
#             answer += '1'
#         n //= 2
#
#         if n == 1:
#             answer += '1'
#             return answer[::-1]
#
#
# import sys
# input = sys.stdin.readline
#
# N = input()
# result = ''
# for i in N:
#     x =
#     result += Oct_to_binary(int(i)).zfill(3)  # 앞에 0을 채워서 문자열을 더해줌
# print(int(result))  # 맨 앞의 0을 제거하기위해 정수형으로 출력

# print(bin(int(input(), 8)[2:]))


#정답
N = int(input(), 8)  # 8진법으로 숫자를 입력 받음
print(bin(N)[2:])  # bin을 쓰면 앞에 0b가 붙으므로, 0b 떼고 문자열의 2번인덱스부터 출력
