from collections import deque

h, w = map(int, input().split())
s = ['#' * (w + 2)] + ['#' + input() + '#' for i in range(h)] + ['#' * (w + 2)]
# print(*s, sep='\n')

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    queue = deque([(si, sj, 0)])
    cost = [[-1] * (w + 2) for _ in range(h + 2)]
    cost[si][sj] = 0
    while queue:
        ci, cj, cc = queue.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if s[ni][nj] == '#':
                continue
            if cost[ni][nj] != -1:
                continue
            queue.append((ni, nj, cc + 1))
            cost[ni][nj] = cc + 1

    return max(map(lambda x: max(x), cost))


ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '.':
            ans = max(ans, bfs(i, j))
print(ans)
