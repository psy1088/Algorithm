def solution(number, k):
    answer = ''
    temp = []
    len_number = len(number)

    for i in range(len_number):
        temp.append((number[i], i))

    temp.sort(key=lambda x: (-int(x[0]), x[1]))  # 값에 대하여 내림차순, 값이 같다면 인덱스 순으로 오름차순

    remain_str = len_number - k
    last_index = 0
    while len(answer) < len_number - k:  # 문자열이 완성될 때까지 반복
        for t in temp:
            if t[1] + remain_str <= len_number and t[1] > last_index:
                answer += t[0]  # 문자열에 추가
                remain_str -= 1  # 남은 문자길이 감소
                last_index = t[1]  # 현재까지 완료된 문자열의 마지막 인덱스를 저장
                temp.remove(t)
                break
    return answer


print(solution("1231234", 3))
