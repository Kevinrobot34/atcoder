import math
n, h = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

a_max = max(a)
throw_cand = []

for i in range(n):
    if b[i] >= a_max:
        throw_cand.append(b[i])
throw_cand.sort()

ans = 0
while h > 0:
    if len(throw_cand) > 0:
        kb = throw_cand.pop()
        h -= kb
        ans += 1
    else:
        ans += math.ceil(h / a_max)
        h -= math.ceil(h / a_max) * a_max

print(ans)
