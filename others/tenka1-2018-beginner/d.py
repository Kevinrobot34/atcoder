n = int(input())

k = 2
while k * (k - 1) // 2 < n:
    k += 1

if n == k * (k - 1) // 2:
    s = [[] for _ in range(k)]
    print('Yes')
else:
    print('No')
