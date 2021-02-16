# p329 기둥과 보 설치
def check(build):
    for part in build:
        x = part[0]
        y = part[1]

        if part[2] == 0:  # 기둥
            # [x,y]에 기둥이 있다면 =>  y좌표 == 0 이거나, (x,y-1)에 기둥존재하거나, (x-1,y)에 보 존재
            if y == 0 or [x, y - 1, 0] in build or [x - 1, y, 1] in build or [x, y, 1] in build:
                continue
            else:
                return False
        elif part[2] == 1:  # 보
            # [x,y] 에 보가 있다면 => (x,y-1)에 기둥존재 or (x+1, y-1)에 기둥존재 or ((x-1,y)and(x+1,y)에 둘다 보 존재)
            if [x, y - 1, 0] in build or [x + 1, y - 1, 0] in build or [x - 1, y, 1] in build and [x + 1, y, 1] in build:
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    while build_frame:
        data = build_frame.pop(0)
        x, y, part = data[0], data[1], data[2]

        if data[3] == 1:  # 설치
            answer.append([x, y, part])
            if not check(answer):
                answer.remove([x, y, part])
        elif data[3] == 0:  # 삭제
            answer.remove([x, y, part])
            print(x, y, "삭제!!", answer)
            if not check(answer):
                answer.append([x, y, part])
                print(x, y, "삭제 안해!!")
    return answer


N = 5
build_Frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

result = solution(N, build_Frame)
print(sorted(result))
