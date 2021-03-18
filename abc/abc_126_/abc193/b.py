n = int(input())

ans = -1
for _ in range(n):
    ai, pi, xi = map(int, input().split())
    if xi > ai and (ans == -1 or pi < ans):
        ans = pi

print(ans)
