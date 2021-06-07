import sys
input = sys.stdin.readline

line = input().rstrip()
result = ''

len_str = len(line)
start = 0
now = 0
while now < len_str:
    # '<' 전까지 문자열의 역순을 저장 후, '>'까지의 문자열을 그대로 저장
    if line[now] == '<': 
        temp = line[start: now] 
        result += temp[::-1]
        start = now

        while line[now] != '>':
            now += 1
        result += line[start:now+1]
        start = now+1

    # 공백 전까지의 문자열을 역순으로 저장
    elif line[now] == ' ':
        temp = line[start: now]
        result += temp[::-1]
        result += ' '
        start = now+1
    
    now += 1

temp = line[start: now]
result += temp[::-1]
print(result)
