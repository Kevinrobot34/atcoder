cookies = list(map(int, input().split()))
n = len(cookies)
s = sum(cookies)

ans = 'No'
for bit in range(1 << n):
    t = sum(cookies[i] for i in range(n) if (bit >> i) & 1)
    if t == s - t:
        ans = 'Yes'
        break

print(ans)
