h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
m = min(min(ai) for ai in a)
ans = sum(sum(aij - m for aij in ai) for ai in a)
print(ans)
