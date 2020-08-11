n = int(input())
cnt_a = cnt_b = cnt_ba = 0
ans = 0
for _ in range(n):
    s = input()
    ans += s.count('AB')
    if s[0] == 'B':
        cnt_b += 1
        if s[-1] == 'A':
            cnt_ba += 1
    if s[-1] == 'A':
        cnt_a += 1

# print(ans, cnt_a, cnt_b)
if cnt_a == cnt_b == n:
    ans += n - 1
elif cnt_ba > 0 and cnt_a == cnt_b == cnt_ba:
    ans += cnt_ba - 1
else:
    ans += min(cnt_a, cnt_b)
print(ans)
