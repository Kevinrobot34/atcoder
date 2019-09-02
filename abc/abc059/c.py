n = int(input())
a = list(map(int, input().split()))

ans0 = ans1 = 0
cs = 0
for i, ai in enumerate(a):
    cs += ai

    if i % 2 == 0:
        if cs < 1:
            ans0 += 1 - cs
            cs = 1
    else:
        if cs > -1:
            ans0 += cs + 1
            cs = -1

cs = 0
for i, ai in enumerate(a):
    cs += ai

    if i % 2 == 0:
        if cs > -1:
            ans1 += cs + 1
            cs = -1
    else:
        if cs < 1:
            ans1 += 1 - cs
            cs = 1

ans = min(ans0, ans1)
print(ans)
