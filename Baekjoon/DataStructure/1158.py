N, K = map(int, input().split())
q = [str(i) for i in range(1, N+1)]
removed = []

index, len_q = 0, len(q)
for _ in range(N):
    index = (index + (K-1)) % len_q
    removed.append(q.pop(index))
    len_q -= 1

print("<%s>" % (", ".join(removed)))
