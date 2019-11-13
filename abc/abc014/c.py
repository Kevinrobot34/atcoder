import sys
input = sys.stdin.readline

n = int(input())
imos = [0] * (10**6 + 5)
for i in range(n):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[b + 1] -= 1

ans = 0
for i in range(10**6 + 1):
    imos[i + 1] += imos[i]
    ans = max(ans, imos[i])

print(ans)
