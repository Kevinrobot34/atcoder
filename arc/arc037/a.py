n = int(input())
m = list(map(int, input().split()))

ans = sum(max(0, 80 - mi) for mi in m)
print(ans)
