import sys

def check(s, t):
    len_s = len(s)
    i = 0
    for j in range(len(t)):
        if s[i] == t[j]:
            i += 1
            if i == len_s:
                return "Yes"
    return "No"


while True:
    line = sys.stdin.readline().strip().split()
    if not line:
        break
    print(check(line[0], line[1]))
