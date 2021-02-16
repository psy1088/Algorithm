# p335 외벽 점검
from itertools import permutations


def solution(n, weak, dist):
    len_weak = len(weak)
    success = False  # 취약지점 전부 점검 가능한지 판단
    min_cnt = len(dist)  # 최소 인원을 총 친구의 수로 초기화

    # weak 리스트를 2배로 늘림
    for i in range(len_weak):
        weak.append(weak[i] + n)

    for order in list(permutations(dist, len(dist))):  # dist 원소의 순서에 따른 모든 경우의 수로 반복하여 최솟값 파악
        for start in range(0, len_weak):  # 시작위치
            dist_index = 0
            position = weak[start] + order[dist_index]  # 한명이 투입된 후의 현재위치
            dist_index += 1
            cnt = 1  # 투입된 인원 수
            inspection = 0  # 점검한 외벽 수

            j = start
            while True:  # start부터 점검
                if position >= weak[j]:  # 현재위치가 해당 취약지점 보다 앞서 있다면 점검 개수 1증가
                    inspection += 1
                    j += 1
                    if inspection == len_weak:  # 점검한 부분이 weak의 개수와 같다면 점검을 다 완료한 것
                        success = True
                        min_cnt = min(min_cnt, cnt)
                        break
                else:
                    if dist_index >= len(order):  # 친구index가 친구의 수 이상이 되면 break
                        break
                    position = weak[j] + order[dist_index]
                    dist_index += 1
                    cnt += 1
    if success:
        return min_cnt
    else:
        return -1


n = 200  # 외벽 길이
weak = [0, 10, 50, 80, 120, 160]  # 취약 지점
dist = [1, 5, 10, 30, 40]  # 이동할 수 있는 거리
print("최종결과", solution(n, weak, dist))