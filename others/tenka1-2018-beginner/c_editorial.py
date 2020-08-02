n = int(input())
a = [int(input()) for _ in range(n)]

cand1 = [0] * n
cand2 = [0] * n
for i in range(n - 1):
    if i % 2 == 0:
        cand1[i] -= 1
        cand1[i + 1] += 1
        cand2[i] += 1
        cand2[i + 1] -= 1
    else:
        cand1[i] += 1
        cand1[i + 1] -= 1
        cand2[i] -= 1
        cand2[i + 1] += 1

cand1.sort()
cand2.sort()
a.sort()

ans = max(
    sum(a[i] * cand1[i] for i in range(n)),
    sum(a[i] * cand2[i] for i in range(n)),
)
print(ans)
