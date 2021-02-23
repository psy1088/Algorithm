# p370 가사 검색
from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

arr = [[] for _ in range(10001)]
reverse_arr = [[] for _ in range(10001)]
cnt = 0


def cal_count(array, l, r):
    b_l = bisect_left(array, l)
    b_r = bisect_right(array, r)

    return b_r - b_l


def find_word_by_list(find_word):
    global cnt
    if find_word[0] == '?':
        find_word = find_word[::-1]
        cnt = cal_count(reverse_arr[len(find_word)], find_word.replace('?', 'a'), find_word.replace('?', 'z'))
    else:
        cnt = cal_count(arr[len(find_word)], find_word.replace('?', 'a'), find_word.replace('?', 'z'))

    return cnt


def solution(words, queries):
    result = [[0] for _ in range(len(queries))]

    for w in words:  # 글자수 별로 리스트에 달리 저장
        arr[len(w)].append(w)
        reverse_arr[len(w)].append(w[::-1])
    for i in range(10001):
        arr[i].sort()
        reverse_arr[i].sort()

    for i in range(len(queries)):
        result[i] = find_word_by_list(queries[i])

    return result


print(solution(words, queries))
