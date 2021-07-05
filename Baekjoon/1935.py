import sys
input = sys.stdin.readline


def calc(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b


n = int(input())
arr = input().rstrip()

operand = {}
for i in range(n):
    operand[chr(ord('A') + i)] = int(input())

stack = []
for s in arr:
    if s.isalpha():
        stack.append(operand[s])
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(calc(a, b, s))

print("%.2lf" % stack[0])
