n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = [(a[i], b[i]) for i in range(n)]
ab.sort(key=lambda x: x[1])
a = [ab[i][0] for i in range(n)]
b = [ab[i][1] for i in range(n)]
ai = [(ab[i][0], i) for i in range(n)]
a.sort()
ai.sort(key=lambda x: x[0])

cond1 = True
for i in range(n):
    if a[i] > b[i]:
        cond1 = False
        break

# cnt : size of cycle which idx0 belongs
# `cnt is n` means there is only 1 cycle
idx = ai[0][1]
cnt = 1
while idx != 0:
    idx = ai[idx][1]
    cnt += 1
# print(a)
# print(ai)
# print(cnt)
if cnt == n:
    # if there is only 1 cycle
    cond2 = False
    for i in range(n - 1):
        if b[i] >= a[i + 1]:
            cond2 = True
            break
else:
    # there are more than 1 cycle
    cond2 = True

ans = "Yes" if cond1 and cond2 else "No"
print(ans)
