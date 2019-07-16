n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

ans = 0
for i in range(n):
    tmp_ans = 0
    for j in range(n):
        if j < i:
            tmp_ans += a[0][j]
        elif j == i:
            tmp_ans += a[0][j] + a[1][j]
        else:
            tmp_ans += a[1][j]

    ans = max(ans, tmp_ans)

print(ans)
