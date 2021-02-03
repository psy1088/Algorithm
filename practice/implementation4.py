## p324 자물쇠와 열쇠

# 리스트 90도 회전
def rotate(key):
    len_key = len(key)
    new_key = [[0] * len_key for _ in range(len_key)]

    for i in range(len_key):
        for j in range(len_key):
            new_key[i][j] = key[len_key - 1 - j][i]
    return new_key


# key와 lock이 맞아떨어지는지 체크
def check(key, big_lock, lock_cnt, x, y):
    len_key = len(key)
    comp_cnt = 0
    for row in range(len_key):
        for col in range(len_key):
            # key값이 1일떄 lock이 0이면 True
            if key[row][col] == 1:
                if big_lock[row + x][col + y] == 0:
                    comp_cnt += 1
                elif big_lock[row + x][col + y] == 1:
                    return False

    if comp_cnt == lock_cnt:
        return True


def solution(key, lock):
    len_lock, len_key = len(lock), len(key)
    len_big = len_lock + (len_key - 1) * 2

    # lock 리스트에서 0의 개수 구함
    lock_cnt = 0
    for i in range(len_lock):
        lock_cnt += lock[i].count(0)

    # Lock 크기를 (key의 크기-1)만큼늘려서 가운데 lock 넣음
    big_lock = [[5] * len_big for _ in range(len_big)]
    for i in range(len_lock):
        for j in range(len_lock):
            big_lock[i + len_key - 1][j + len_key - 1] = lock[i][j]

    # big_lock에 key를 0,0부터 차례대로 완전탐색
    for _ in range(4):
        for x in range(len_lock + len_key - 1):
            for y in range(len_lock + len_key - 1):
                if check(key, big_lock, lock_cnt, x, y):
                    return True
        key = rotate(key)
    return False
