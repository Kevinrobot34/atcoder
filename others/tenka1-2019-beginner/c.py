n = int(input())
s = input()

b_cnt = [0] * (n + 1)
for i in range(n):
    if s[i] == '#':
        b_cnt[i + 1] = b_cnt[i] + 1
    else:
        b_cnt[i + 1] = b_cnt[i]

ans = n
for i in range(n + 1):
    ans = min(ans, ((n - i) - (b_cnt[n] - b_cnt[i])) + b_cnt[i])

print(ans)
