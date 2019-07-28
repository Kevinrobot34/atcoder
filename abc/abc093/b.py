a, b, k = map(int, input().split())

ans = {i for i in range(a, min(a+k, b))} | {i for i in range(max(a, b+1-k), b+1)}
ans = sorted(ans)
for i in ans:
    print(i)
