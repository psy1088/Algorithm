import sys
input = sys.stdin.readline

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

time1 = 60*60*h1 + 60*m1 + s1
time2 = 60*60*h2 + 60*m2 + s2

if time1 < time2:
    res = time2 - time1
else:
    res = (24 * 60 * 60 + time2) - time1

h = res // 60 // 60
m = res // 60 % 60
s = res % 60

print("%02d:%02d:%02d" % (h, m, s))
