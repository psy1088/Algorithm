# 1번. 문자열 정수로 출력
def solution(s):
    if s[0] == '-':
        num = int(s[1:]) * -1
    else:
        num = int(s)
    return num


# 2번. 휴대폰 키패드 조작
def solution(numbers, hand):
    answer = ''
    keypad = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']

    left, right = keypad.index('*'), keypad.index('#')
    for i in range(len(numbers)):
        n = numbers[i]
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left = keypad.index(n)
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right = keypad.index(n)
        else:  # 2,5,8,0 일 때
            n_index = keypad.index(n)
            l_dist = abs(left // 3 - n_index // 3) + abs(left % 3 - n_index % 3)
            r_dist = abs(right // 3 - n_index // 3) + abs(right % 3 - n_index % 3)

            if l_dist < r_dist:
                answer += 'L'
                left = keypad.index(n)
            elif l_dist > r_dist:
                answer += 'R'
                right = keypad.index(n)
            else:  # 거리가 같다면
                if hand == "left":
                    answer += 'L'
                    left = keypad.index(n)
                else:
                    answer += 'R'
                    right = keypad.index(n)

    return answer
