from bisect import bisect_left
n = int(input())
a = [int(input()) for _ in range(n)]
a_sorted = sorted(list(set(a)))

for i in range(n):
    print(bisect_left(a_sorted, a[i]))
