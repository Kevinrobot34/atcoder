import math
q = int(input())
l = []
r = []
for i in range(q):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

r_max = max(r) + 10
is_prime = [True] * (r_max+1)
is_prime[0] = is_prime[1] = False
for i in range(2, r_max):
    if is_prime[i]:
        for j in range(2, r_max // i + 1):
            is_prime[i*j] = False

# print(is_prime)
a = [0] * r_max
for i in range(3, r_max):
    a[i] = a[i-1]
    if is_prime[i] and is_prime[(i+1)//2]:
        a[i] += 1
# print(a)

for i in range(q):
    print(a[r[i]] - a[l[i]-1])
