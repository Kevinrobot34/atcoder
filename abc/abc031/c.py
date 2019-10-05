n = int(input())
a = list(map(int, input().split()))

ans = -10**5
for tak_i in range(n):
    aok_cand = -10**5
    tak_cand = -10**5
    for aok_i in range(n):
        if aok_i == tak_i:
            continue

        if aok_i < tak_i:
            aok_score = sum(a[aok_i+1:tak_i+1:2])
            tak_score = sum(a[aok_i:tak_i+1:2])
        else:
            aok_score = sum(a[tak_i+1:aok_i+1:2])
            tak_score = sum(a[tak_i:aok_i+1:2])

        # print(aok_i, tak_i, aok_score, tak_score)
        if aok_score > aok_cand:
            aok_cand = aok_score
            tak_cand = tak_score

    if ans < tak_cand:
        ans = tak_cand

print(ans)
