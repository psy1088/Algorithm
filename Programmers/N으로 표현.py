def solution(N, number):
    dp = [[]]

    for i in range(1, 9): # N의 개수
        all_case = set()
        all_case.add(int(str(N) * i))
        
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2:
                        all_case.add(op1 // op2)
        if number in all_case:
            return i
        dp.append(all_case)
    
    return -1
