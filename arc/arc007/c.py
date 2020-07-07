c = input()
n = len(c)

ans = n
for bit in range(1 << n):
    if bit % 2 == 0:
        continue
    m = 0
    check = [False] * (2 * n)
    for i in range(n):
        if (bit >> i) & 1:
            m += 1
            for j in range(n):
                if c[j] == 'o':
                    check[i + j] = True
                    if i + j + n < 2 * n:
                        check[i + j + n] = True
    # print(bin(bit), check)

    cnt = 0
    check.append(False)
    for i in range(2 * n + 1):
        if check[i]:
            cnt += 1
        else:
            if cnt >= n:
                ans = min(ans, m)
                break
            cnt = 0

print(ans)
