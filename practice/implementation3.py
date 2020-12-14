# p323 문자열 압축
def solution(s):
    answer = len(s)

    for step in range(1, len(s)//2 + 1): # 문자열의 총 길이의 1/2만큼까지만 기준으로 잡아
        compressed = ""
        prev = s[0:step] # 기준이 되는 문자열 저장
        cnt = 1
        for j in range(step, len(s), step): # step만큼 증가시켜가며 비교
            if prev == s[j:j+step]: # 같다면 cnt 증가
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt > 1 else prev
                prev = s[j:j+step]
                cnt = 1
        compressed += str(cnt) + prev if cnt > 1 else prev
        answer = min(answer, len(compressed))
    return answer

s = input() # 입력 문자열
print(solution(s))




