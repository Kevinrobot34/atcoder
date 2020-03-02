n = int(input())


def func(x):
    while x >= 10:
        x //= 10
    return x


cnt = [[0] * 10 for _ in range(10)]
for i in range(1, n + 1):
    digit_end = i % 10
    digit_start = func(i)
    cnt[digit_start][digit_end] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)
