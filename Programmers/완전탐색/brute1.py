def solution(answers):
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    result = []

    len1, len2, len3 = len(arr1), len(arr2), len(arr3)
    for i in range(len(answers)):
        if answers[i] == arr1[i % len1]:
            cnt[0] += 1
        if answers[i] == arr2[i % len2]:
            cnt[1] += 1
        if answers[i] == arr3[i % len3]:
            cnt[2] += 1

    max_val = max(cnt)
    for i in range(3):
        if cnt[i] == max_val:
            result.append(i + 1)

    return result
