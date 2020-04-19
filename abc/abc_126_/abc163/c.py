from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)

for i in range(len(a)):
    d[a[i]] += 1

for i in range(1, n + 1):
    print(d[i])
