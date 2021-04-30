from itertools import combinations

def check(dict):
    arr = []
    if not dict:
        return arr
    else:
        max_val = max(list(dict.values()))
        if max_val < 2:
            return arr
        
        for d in dict:
            if dict[d] == max_val:
                arr.append(''.join(d))
    return arr


def solution(orders, course):
    res = []
    for _len in course:
        dict = {}
        for order in orders:
            if len(order) < _len:
                continue
            for case in combinations(order, _len):
                case = tuple(sorted(case))
                if case in dict:
                    dict[case] += 1
                else:
                    dict[case] = 1
        
        for x in check(dict):
            res.append(x)
        
    return sorted(res)
