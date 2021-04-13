def check(add_arr): # 만들 수 있는 단어의 개수 구함
    res = 0
    for word in words:
        flag = True
        for x in word:
            if x not in add_arr:
                flag = False
                break
        if flag:
            res += 1
    return res


from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N=단어 개수, K=사용할 글자 수

if K < 5:
    print(0)
    exit(0)
elif K == 26:
    print(N)
    exit(0)
else:
    baseset = set('acint')
    words = [] # 모든 단어를 위해 필요한 문자들 리스트
    need_word = []
    for i in range(N): # a c i n t가 아닌 문자 중에 중복을 제외하고 입력받음
        words.append(set(input().rstrip()) - baseset)
        if len(words[i]) <= K-5: # 특정 단어가 K-5보다 크면, 애초에 만들 수 없는 단어임
            need_word += words[i]
    need_word = set(need_word)

    max_cnt = 0
    if len(need_word) < K-5: # 모든 단어를 만드는데 필요한 단어 개수가 K-5보다 작으면, 바로 계산해줌
        max_cnt = check(need_word)
    else: # 아니면, 조합으로 경우의 수 구해서 계산
        for case in combinations(need_word, K-5):
            cnt = check(case)
            max_cnt = max(max_cnt, cnt)

    print(max_cnt)