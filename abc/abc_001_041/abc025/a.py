s = input()
n = int(input()) - 1

cand = []
for si in s:
    for sj in s:
        cand.append(si + sj)
ans = cand[n]
print(ans)
