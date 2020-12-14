# p324 자물쇠와 열쇠

# 자물쇠의 (길이-1)*2 + 길이해가지고
# 키를 하나씩 싹 대보면서 비교해봐 합이 only 1이되는지!! 2가 되면 안되지

arr_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
arr_lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


# 이차원 행렬 시계방향으로 90도 회전
def rotation_matrix_90degree(x):
    row = len(x)
    col = len(x[0])
    trans_arr = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            trans_arr[i][j] = x[row - 1 - j][i]
    return trans_arr


# 자물쇠가 다 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    lock_length = len(lock)
    key_length = len(key)

    new_lock = [[0] * (lock_length * 3) for _ in range(lock_length * 3)]

    for i in range(lock_length):
        for j in range(lock_length):
            new_lock[i + lock_length][j + lock_length] = lock[i][j]

    # 4가지 방향 회전하면서 확인하기
    for i in range(4):
        key = rotation_matrix_90degree(key)
        for a in range(lock_length * 2):
            for b in range(lock_length * 2):
                for c in range(key_length):
                    for d in range(key_length):
                        new_lock[a + c][b + d] += key[c][d]
                if check(new_lock):
                    return True
                for c in range(key_length):
                    for d in range(key_length):
                        new_lock[a + c][b + d] -= key[c][d]
    return False


print(solution(arr_key, arr_lock))
