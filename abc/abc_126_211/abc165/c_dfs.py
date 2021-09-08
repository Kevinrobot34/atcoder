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
l = [0] * n
l[0] = 1


def dfs(l_len):
    global l, ans
    if l_len == n:
        ans = max(ans, calc(l))
        return

    for i in range(l[l_len - 1], m + 1):
        l[l_len] = i
        dfs(l_len + 1)


dfs(1)
print(ans)
