import sys
input = sys.stdin.readline

n, c = map(int, input().split())
sushi = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

cand1 = [0] * n
v_sum = 0
for i in range(n):
    v_sum += sushi[i][1]
    cand1[i] = v_sum - sushi[i][0]
    if i > 0:
        cand1[i] = max(cand1[i], cand1[i-1])

cand2 = [0] * n
v_sum = 0
for i in reversed(range(n)):
    v_sum += sushi[i][1]
    cand2[i] = v_sum - (c - sushi[i][0])
    if i != n - 1:
        cand2[i] = max(cand2[i], cand2[i+1])

ans = max(ans, max(cand1), max(cand2))

v_sum = 0
for i in reversed(range(1, n)):
    v_sum += sushi[i][1]
    ans = max(ans, v_sum - (c - sushi[i][0]) * 2 + cand1[i-1])

v_sum = 0
for i in range(n-1):
    v_sum += sushi[i][1]
    ans = max(ans, v_sum - sushi[i][0] * 2 + cand2[i+1])

print(ans)
