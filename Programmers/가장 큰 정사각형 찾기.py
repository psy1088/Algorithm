def solution(board):
    row, col = len(board), len(board[0])
    for r in range(1, row):
        for c in range(1, col):
            if board[r][c] == 0:
                continue
            min_val = min(board[r-1][c], board[r][c-1], board[r-1][c-1])
            board[r][c] = min_val + 1
    
    max_val = 0
    for line in board:
        max_val = max(max_val, max(line))
    return max_val * max_val
