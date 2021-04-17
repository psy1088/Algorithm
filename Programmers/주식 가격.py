def solution(prices):
    len_prices = len(prices)
    answer = [0] * len_prices
    
    for i in range(len_prices):
        for j in range(i+1, len_prices):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break

    return answer
