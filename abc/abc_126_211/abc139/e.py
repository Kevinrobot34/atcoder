from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

def calc_idx(x, y):
    if x > y:
        x, y = y, x
    return x + y*(y-1)//2

# create graphs & calc indegree
n_game = n * (n-1) // 2
edge = [[] for i in range(n_game)]
indegree = [0] * n_game
for i in range(n):
    ai = list(map(int, input().split()))

    for j in range(1, n-1):
        g1 = calc_idx(i, ai[j-1]-1)
        g2 = calc_idx(i, ai[j]-1)
        edge[g1].append(g2)
        indegree[g2] += 1


ans = 0
cand = deque([(i, 1) for i in range(n_game) if indegree[i] == 0])
n_ts = 0
while len(cand) > 0:
    u, day = cand.popleft()
    ans = max(ans, day)
    n_ts += 1
    for v in edge[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            cand.append((v, day+1))

if n_ts != n_game:
    ans = -1

print(ans)
