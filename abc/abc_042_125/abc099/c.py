n = int(input())

ans = n
for i in range(n+1):
    tmp_ans = 0
    m = i
    while m > 0:
        tmp_ans += m % 6
        m = m // 6
    m = n - i
    while m > 0:
        tmp_ans += m % 9
        m = m // 9

    ans = min(ans, tmp_ans)

print(ans)
