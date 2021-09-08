n = int(input())
a = list(map(int, input().split()))

ia = list(enumerate(a))
for _ in range(n - 1):
    ib = []
    for j in range(len(ia) // 2):
        i0, a0 = ia[2 * j + 0]
        i1, a1 = ia[2 * j + 1]
        if a0 > a1:
            ib.append(ia[2 * j + 0])
        else:
            ib.append(ia[2 * j + 1])
    ia = ib

i0, a0 = ia[0]
i1, a1 = ia[1]
ans = i1 if a0 > a1 else i0
ans += 1
print(ans)
