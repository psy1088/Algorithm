def check(stack, doll):
    if not stack: # 스택이 비어있으면 False
        return False
    if stack[-1] == doll:
        return True
    else:
        return False

    
def solution(board, moves):
    stack = []
    count = 0
    len_board = len(board)
    
    for m in moves:
        for i in range(len_board):
            doll = board[i][m-1]
            if doll == 0:
                continue
            if check(stack, doll):
                stack.pop()
                count += 2
            else:
                stack.append(doll)
                
            board[i][m-1] = 0
            break

    return count
