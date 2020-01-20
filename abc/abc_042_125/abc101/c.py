import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

print(1 + math.ceil((n-k) / (k-1)))
