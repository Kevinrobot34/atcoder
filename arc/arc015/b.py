n = int(input())
ans = [0] * 6
for _ in range(n):
    a, b = map(float, input().split())
    if a >= 35.0:
        ans[0] += 1
    elif a >= 30.0:
        ans[1] += 1
    elif a >= 25.0:
        ans[2] += 1
    elif a < 0.0:
        ans[5] += 1

    if b >= 25.0:
        ans[3] += 1

    if b < 0.0 and a >= 0.0:
        ans[4] += 1

print(*ans)
