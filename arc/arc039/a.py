a, b = map(int, input().split())

str_a, str_b = str(a), str(b)
ans = a - b
for i in range(100, 1000):
    for j in range(100, 1000):
        cnt = 0
        str_i = str(i)
        str_j = str(j)
        for k in range(3):
            if str_i[k] != str_a[k]:
                cnt += 1
            if str_j[k] != str_b[k]:
                cnt += 1
        if cnt > 1:
            continue

        ans = max(ans, i - j)

print(ans)
