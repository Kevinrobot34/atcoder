import sys
n = int(input())

u = 1
w = 0
dist1 = [0] * (n + 1)
for v in range(2, n + 1):
    print(f'? {u} {v}')
    sys.stdout.flush()
    dist1[v] = int(input())
    if dist1[v] > dist1[w]:
        w = v

ans = 0
for v in range(1, n + 1):
    if v == w:
        continue
    print(f'? {w} {v}')
    sys.stdout.flush()
    ans = max(ans, int(input()))

print(f'! {ans}')
