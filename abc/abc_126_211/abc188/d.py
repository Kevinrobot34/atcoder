import sys
input = sys.stdin.readline


def compress_coordinate(x: list, key=None, reverse=False):
    zipped = {}
    unzipped = {}
    for i, xi in enumerate(sorted(set(x), key=None, reverse=reverse)):
        zipped[xi] = i
        unzipped[i] = xi
    return zipped, unzipped


n, c = map(int, input().split())

ab = [0, 10**9 + 5]
abc = []
for _ in range(n):
    ai, bi, ci = map(int, input().split())
    ab.append(ai)
    ab.append(bi + 1)
    abc.append((ai, bi, ci))

zipped, unzipped = compress_coordinate(ab)

imos = [0] * len(zipped)
for ai, bi, ci in abc:
    imos[zipped[ai]] += ci
    imos[zipped[bi + 1]] -= ci

for i in range(len(imos) - 1):
    imos[i + 1] += imos[i]

ans = 0
for i in range(len(imos) - 1):
    ans += min(imos[i], c) * (unzipped[i + 1] - unzipped[i])

print(ans)
