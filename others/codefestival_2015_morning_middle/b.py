def z_algorithm(s):
    n = len(s)
    z = [0] * n
    z[0] = n

    i = 1
    lcp = 0
    while i < n:
        while i + lcp < n and s[i + lcp] == s[lcp]:
            lcp += 1
        z[i] = lcp

        if lcp == 0:
            i += 1
            continue

        k = 1
        while i + k < n and k + z[k] < lcp:
            z[i + k] = z[k]
            k += 1
        i += k
        lcp -= k

    return z


n = int(input())
s = input()

l = 0
for i in range(n):
    z = z_algorithm(s[i:])
    for j in range(1, len(z)):
        l = max(l, min(z[j], j, len(z) - j))

ans = n - l * 2
print(ans)
