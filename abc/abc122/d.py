from collections import defaultdict
n = int(input())
MOD = 10 ** 9 + 7

s = "ATGC"
t = ["AGC", "ACG", "GAC"]
d = [defaultdict(int), {x+y+z: 1 for x in s for y in s for z in s if x+y+z not in t}]
# d = [{"": 1}, defaultdict(int)]

# print(d[0])
for i in range(4, n+1):
    a = i%2
    b = (i-1)%2

    d[a] = defaultdict(int)
    for k in d[b]:
        for c in s:
            if "AGC" not in [k[1:]+c, k[0]+k[2]+c, k[2]+k[1]+c, k[1]+c+k[2], k[0]+k[1]+c]:
                d[a][k[1:]+c] += d[b][k]
                d[a][k[1:]+c] %= MOD

print(sum(d[n%2].values()) % MOD)
