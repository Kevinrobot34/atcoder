n = int(input())
info = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    info[i] = [tuple(map(int, input().split())) for _ in range(a)]

ans = 0
for bit in range(1 << n):
    flag = True
    cnt = 0
    for i in range(n):
        if (bit >> i) & 1:
            cnt += 1
        else:
            continue

        for x, y in info[i]:
            b = (bit >> (x - 1)) & 1
            if b != y:
                flag = False
                break
        if not flag:
            break
    if flag:
        ans = max(ans, cnt)

print(ans)
