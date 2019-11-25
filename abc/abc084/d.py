import sys
import math
input = sys.stdin.readline


def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if i * i > n:
            break
        if is_prime[i]:
            for j in range((n - i * i) // i + 1):
                is_prime[i * i + i * j] = False
    return is_prime


q = int(input())
l = []
r = []
for i in range(q):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

r_max = max(r)
is_prime = eratosthenes(r_max)
a = [0] * (r_max + 1)
for i in range(3, r_max + 1):
    a[i] = a[i - 1]
    if is_prime[i] and is_prime[(i + 1) // 2]:
        a[i] += 1
# print(a)

for i in range(q):
    print(a[r[i]] - a[l[i] - 1])
