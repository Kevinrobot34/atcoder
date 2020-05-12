from collections import deque
n = int(input())
MOD = 10007

a = deque([0, 0, 1])
if n < 3:
    ans = a[n - 1]
else:
    n -= 3
    while n > 0:
        a.append((a[0] + a[1] + a[2]) % MOD)
        a.popleft()
        n -= 1
    ans = a[-1]

print(ans)
