n = int(input())
a = list(map(int, input().split()))

a_sum = sum(a)
if a_sum % n != 0:
    ans = -1
else:
    m = a_sum // n
    ans = 0
    cnt_i = 1
    cnt_s = a[0]
    for i in range(1, n):
        if cnt_s == m * cnt_i:
            cnt_i = 1
            cnt_s = a[i]
        else:
            cnt_i += 1
            cnt_s += a[i]
            ans += 1

print(ans)
