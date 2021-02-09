# p346 괄호변환
def balance_str(p):  # 균형잡힌 괄호 문자열의 인덱스 리턴
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i


def check(x):  # 올바른 문자열인지 체크
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        else:  # 오른쪽 괄호일 때
            if not stack:  # 스택이 비어있다면 올바르지 않아
                return False
            else:  # 비어있지 않다면 왼쪽괄호 pop
                stack.pop()
    if not stack:  # 문자열을 전부 검사한 뒤, 스택이 비어있다면 올바른 문자열
        return True
    else:
        return False


def solution(p):
    answer = ''
    if p == '':
        return answer

    # p를 u, v로 분해
    index = balance_str(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check(u):  # u가 올바른 문자열이라면 문자열 v로 재귀
        answer = u + solution(v)
    else:  # 올바른 놈이 아니면,
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 첫번째, 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer


p = ")(((())())"
print(solution(p))
