n, c = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

ans = [n * (n + 1) // 2] * c
prev_idx = [-1] * c

for i, ai in enumerate(a):
    l = i - prev_idx[ai] - 1
    ans[ai] -= l * (l + 1) // 2
    prev_idx[ai] = i

for i in range(c):
    l = n - prev_idx[i] - 1
    ans[i] -= l * (l + 1) // 2

print(*ans, sep='\n')
