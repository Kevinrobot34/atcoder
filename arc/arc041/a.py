x, y = map(int, input().split())
k = int(input())

ans = (x - max(0, k - y)) + min(k, y)
print(ans)
