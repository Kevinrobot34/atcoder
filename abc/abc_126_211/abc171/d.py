n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (10**5 + 10)
for ai in a:
    cnt[ai] += 1

ans = []
s = sum(a)
q = int(input())
for _ in range(q):
    b, c = map(int, input().split())
    s = s + (c - b) * cnt[b]
    ans.append(s)
    cnt[c] += cnt[b]
    cnt[b] = 0

print(*ans, sep='\n')
