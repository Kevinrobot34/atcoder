n, m = map(int, input().split())
a = list(map(int, input().split()))
pos = [[-1] for _ in range(n)]
for i, ai in enumerate(a):
    pos[ai].append(i)
for i in range(n):
    pos[i].append(n)

ans = n
for i in range(n):
    for j in range(len(pos[i]) - 1):
        if pos[i][j + 1] - pos[i][j] > m:
            ans = i
            break
    if ans < n:
        break
print(ans)
