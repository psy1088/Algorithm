from itertools import combinations

def solution(relation):
    row, col = len(relation), len(relation[0])
    list_col = [i for i in range(col)]
    candidates = []

    # 유일성 조건 확인
    def unique(case):
        temp = set()
        for r in range(row):
            s = ''
            for c in case:
                s += relation[r][c]
            temp.add(s)

        if len(temp) == row:
            return True
        else:
            return False    

    # 최소성 조건 확인
    def minimality(case):
        for candidate in candidates: # 집합A,B를 비교할 때, A,B의 교집합이 A와 같다면 False
            if len(set(candidate) & set(case)) == len(set(candidate)):
                return False
        return True


    for i in range(1, col+1):
        for case in combinations(list_col, i):
            if unique(case) and minimality(case):
                candidates.append(case)

    return len(candidates)
