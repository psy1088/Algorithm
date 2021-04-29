def solution(lottos, win_nums):
    cnt, zero_cnt = 0, 0
    for num in lottos:
        if num == 0:
            zero_cnt += 1
        elif num in win_nums:
            cnt += 1
    
    best_win = 7 - (cnt + zero_cnt) if (cnt + zero_cnt) > 0 else 6
    worst_win = 7 - cnt if cnt > 0 else 6
    
    return [best_win, worst_win]
