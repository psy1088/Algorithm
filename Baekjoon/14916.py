n = int(input())
if n in [1, 3]:
    print(-1)
else:
    five, two = 0, 0
    
    five = n // 5
    if (n-(five*5)) % 2 != 0:
        five -= 1
    
    n -= five*5
    two = n // 2
    
    print(five+two)
