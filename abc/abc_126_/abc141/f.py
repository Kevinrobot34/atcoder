n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

s = 0
for a_i in a:
    s ^= a_i
# print(s)

c = [(~s) & a_i for a_i in a]
base = []
for c_i in c:
    for base_j in base:
        c_i = min(c_i, c_i ^ base_j)
    if c_i != 0:
        for j in range(len(base)):
            base[j] = min(base[j], base[j] ^ c_i)
        base.append(c_i)
        base.sort(reverse=True)

# print(base)
t = 0
for base_j in base:
    t ^= base_j
# print(t)
ans = s + t * 2
print(ans)
