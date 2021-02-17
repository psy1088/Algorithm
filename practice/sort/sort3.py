# # p361 실패율
def solution(N, stages):
    result = {}
    cnt_remain = len(stages)  # 남은 도전자 수

    for i in range(1, N+1):
        if cnt_remain != 0:  # 도전자 수가 0이 아니면~
            cnt_fail = stages.count(i)  # 해당 스테이지에서 실패한 도전자 수
            result[i] = cnt_fail / cnt_remain  # 딕셔너리에 key: value저장 { i: fail_rate }
            cnt_remain -= cnt_fail
        else:
            result[i] = 0

    return sorted(result, key=lambda x: (-result[x]))  # 딕셔너리의 value(실패율)를 기준으로 내림차순 정렬


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
