def solution(skill, skill_trees):
    dict = {}
    for i in range(len(skill)):
        dict[skill[i]] = i
    
    res = 0
    for skill_tree in skill_trees:
        possible = True
        order = 0
        for c in skill_tree:
            if c in dict:
                if dict[c] == order:
                    order += 1
                else:
                    possible = False
                    break
        if possible:
            res += 1
    
    return res


# from collections import deque

# def solution(skill, skill_trees):
#     res = 0
    
#     for skill_tree in skill_trees:
#         skill_q = deque(skill)
#         possible = True

#         for c in skill_tree:
#             if c in skill_q:
#                 if c != skill_q.popleft():
#                     possible = False
#                     break
#         if possible:
#             res += 1
    
#     return res
