n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

k_subset = [k]
for i in range(len(bin(k)) - 2):
    if (k >> i) & 1:
        x = k & ~(1 << i)  # remove i-th bit
        x = x | ((1 << i) - 1)  # add 1 to j-th bit (j<i)
        k_subset.append(x)

ans = max(sum(b for a, b in ab if a | x == x) for x in k_subset)

print(ans)
