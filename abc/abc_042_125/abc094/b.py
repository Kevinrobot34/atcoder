from bisect import bisect_left

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

b = bisect_left(a, x)
print(min(b, m-b))
