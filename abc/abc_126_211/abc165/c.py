from itertools import combinations_with_replacement

n, m, q = map(int, input().split())
cond = []
for _ in range(q):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    cond.append((a, b, c, d))


def calc(l):
    score = 0
    for a, b, c, d in cond:
        if l[b] - l[a] == c:
            score += d
    return score


ans = 0
for l in combinations_with_replacement(range(1, m + 1), n):
    cand = calc(l)
    ans = max(ans, cand)

print(ans)
