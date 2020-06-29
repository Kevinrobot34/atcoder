n = int(input())
s = 0
for _ in range(n):
    a, b = map(int, input().split())
    s += a * b

ans = s * 105 // 100
print(ans)
