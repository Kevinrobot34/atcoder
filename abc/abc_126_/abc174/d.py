n = int(input())
c = input()

cnt_r = [0] * (n + 1)
for i in range(n):
    if c[i] == 'R':
        cnt_r[i + 1] = cnt_r[i] + 1
    else:
        cnt_r[i + 1] = cnt_r[i]

ans = n
for i in range(n + 1):
    right_r = cnt_r[n] - cnt_r[i]
    left_w = i - cnt_r[i]
    ans = min(ans, max(right_r, left_w))

print(ans)
