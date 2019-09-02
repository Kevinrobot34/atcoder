n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()

ans = sum(s)
if ans % 10 == 0:
    for i in range(n):
        if s[i] % 10 != 0:
            ans -= s[i]
            break
    if ans % 10 == 0:
        ans = 0

print(ans)
