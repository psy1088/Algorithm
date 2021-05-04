import copy

def solution(money1):
    len_money = len(money1)
    money2 = copy.deepcopy(money1)
    
    # 첫번째 집을 털 경우 => 마지막 집을 못 털음
    money1[1] = money1[0]
    for i in range(2, len_money-1):
        money1[i] = max((money1[i-2]+money1[i]), money1[i-1])

    # 두번째 집을 털 경우 => 첫번째 집을 못 털음
    money2[0] = 0
    for i in range(2, len_money):
        money2[i] = max((money2[i-2]+money2[i]), money2[i-1])
    
    return max(max(money1), max(money2))
