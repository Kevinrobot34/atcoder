from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for ai in a:
    d[ai] += 1


n1 = n2 = 0
for k, v in d.items():
    if v >= 3:
        if v % 2 == 0:
            d[k] = 2
        else:
            d[k] = 1

    if d[k] == 1:
        n1 += 1
    else:
        n2 += 1

# print(d)
# print(n1, n2)
n1 += n2 - n2 % 2
n2 = n2 % 2

ans = n1

print(n1)
