import math

def solution(w, h):
    path = w + h - math.gcd(w, h)
    return w*h - path
