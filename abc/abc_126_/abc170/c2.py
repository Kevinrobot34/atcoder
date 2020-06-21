x, n = map(int, input().split())
p = list(map(int, input().split()))
p = set(p)

cand1 = x
while cand1 in p:
    cand1 -= 1

cand2 = x
while cand2 in p:
    cand2 += 1

ans = cand1 if abs(cand1 - x) <= abs(cand2 - x) else cand2
print(ans)
