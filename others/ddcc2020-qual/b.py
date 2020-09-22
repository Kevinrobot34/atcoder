n = int(input())
a = list(map(int, input().split()))

a_sum = sum(a)
x = 0
y = 0
for i in range(n):
    x += a[i]

    if x * 2 >= a_sum:
        y = a[i]
        break

ans = min(abs(2 * x - a_sum), abs(a_sum - 2 * (x - y)))
print(ans)
