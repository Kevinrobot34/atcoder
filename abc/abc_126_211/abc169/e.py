n = int(input())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
a.sort()
b.sort()

if n % 2 == 1:
    a_median = a[(n - 1) // 2]
    b_median = b[(n - 1) // 2]
    # print(a_median, b_median)
    ans = b_median - a_median + 1
else:
    a_median = (a[n // 2 - 1] + a[n // 2])
    b_median = (b[n // 2 - 1] + b[n // 2])
    # print(a_median, b_median)
    ans = b_median - a_median + 1
print(ans)
