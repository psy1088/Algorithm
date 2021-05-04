# 1번 풀이
def solution(n, lost, reserve):
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        elif l - 1 in reserve:
            reserve.remove(l - 1)
        elif l + 1 in reserve and l + 1 not in lost:
            reserve.remove(l + 1)
        else:
            n -= 1

    return n

# 2번 풀이
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]

#     for l in _lost:
#         if l-1 in _reserve:
#             _reserve.remove(l-1)
#         elif l+1 in _reserve:
#             _reserve.remove(l+1)
#         else:
#             n -= 1
#     return n
