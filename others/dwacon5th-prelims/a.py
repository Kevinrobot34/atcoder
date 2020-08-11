n = int(input())
a = list(map(int, input().split()))
a_ave = sum(a) / n

ans = 0
for i in range(1, n):
    if abs(a[ans] - a_ave) > abs(a[i] - a_ave):
        ans = i

print(ans)
