import sys
input = sys.stdin.readline


def check(line):
    vowel = ['a', 'e', 'i', 'o', 'u']
    v_cnt = 0

    if line[0] in vowel:
        al = 'v' # v(모음) / c(자음)
        v_cnt += 1
    else:
        al = 'c'

    cnt = 1
    prev = line[0]

    for i in range(1, len(line)):
        if line[i] == prev: # 같은 글자가 연속 두번이면 안됨
            if line[i] != 'e' and line[i] != 'o':
                return False
        prev = line[i]

        if line[i] in vowel:
            now = 'v'
            v_cnt += 1 # 모음 개수 체크
        else:
            now = 'c'

        if al == now:
            cnt += 1
        else:
            cnt = 1
            al = now
        if cnt == 3: # 모음 or 자음이 연속 3개이면 안됨
            return False

    if v_cnt == 0: # 모음은 반드시 하나를 포함해야함
        return False
    return True


while True:
    line = input().strip()
    if line == 'end':
        break

    if check(line):
        print("<%s> is acceptable." % line)
    else:
        print("<%s> is not acceptable." % line)
