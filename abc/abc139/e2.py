from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
a = [deque(map(lambda x: int(x)-1, input().split())) for _ in range(n)]

remain_games = n * (n-1) // 2
ans = 0
while remain_games:
    flag = [0] * n
    update = False
    for i in range(n):
        if len(a[i]) == 0 or len(a[ a[i][0] ]) == 0:
            continue
        if flag[i] == 0 and a[ a[i][0] ][0] == i and flag[ a[i][0] ] == 0:
            b = a[i].popleft()
            _ = a[b].popleft()
            flag[i] = 1
            flag[b] = 1
            remain_games -= 1
            # print(ans, i, b)
            update = True
    if not update:
        ans = -1
        break
    ans += 1

print(ans)
