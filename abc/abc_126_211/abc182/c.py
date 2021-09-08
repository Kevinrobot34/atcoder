n = input()

k = len(n)
ans = k
for bit in range(1, 1 << k):
    m = ''.join(n[i] for i in range(k) if (bit >> i) & 1 == 1)
    k2 = len(m)
    # print(bit, m)
    if int(m) % 3 == 0:
        ans = min(ans, k - k2)

if ans == k:
    ans = -1
print(ans)
