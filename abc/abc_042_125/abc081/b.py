n = int(input())
a = list(map(int, input().split()))

ans = 10 ** 9
for i in range(n):
    tmp_ans = 0
    while a[i] % 2 ==0:
        tmp_ans += 1
        a[i] = a[i] // 2

    ans = min(ans, tmp_ans)

print(ans)
