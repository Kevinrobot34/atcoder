from collections import defaultdict, Counter

def comb(n: int, k: int) -> int:
    ans = 1
    for i in range(1, k+1):
        ans *= n - i + 1
        ans //= i
    return ans

n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
c = Counter(v)

cand = defaultdict(int)
for m in range(a, b+1):
    s = sum(v[:m])
    k = len(list(filter(lambda x: x == v[m-1], v[:m])))
    l = c[v[m-1]]

    cand[s / m] += comb(l, k)

# print(cand)
ans1 = max(cand.keys())
print(ans1)
print(cand[ans1])
