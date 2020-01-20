n, k = map(int, input().split())
r, s, p = map(int, input().split())
score = {'r': p, 's': r, 'p': s}
t = list(input())

ans = 0
for i in range(k):
    # print(i, score[t[i]], ans)
    ans += score[t[i]]
    j = i + k
    f = 0
    while j < n:
        if t[j] != t[j - k]:
            ans += score[t[j]]
            # print(j, score[t[j]], ans)
        else:
            t[j] = '-'
        j += k
    # print(ans)

print(ans)
