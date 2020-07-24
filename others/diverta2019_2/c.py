n = int(input())
a = list(map(int, input().split()))
cnt_m = len(list(filter(lambda x: x < 0, a)))

if cnt_m == 0:
    i_m = a.index(min(a))
    i_p = (i_m + 1) % n
elif cnt_m == n:
    i_p = a.index(max(a))
    i_m = (i_p + 1) % n
else:
    i_m = i_p = -1
    for i in range(n):
        if i_m == -1 and a[i] < 0:
            i_m = i
        if i_p == -1 and a[i] >= 0:
            i_p = i

is_used = [False] * n
ans = []

is_used[i_m] = True
is_used[i_p] = True
s_m = a[i_m]
s_p = a[i_p]
for i in range(n):
    if not is_used[i]:
        if a[i] >= 0:
            ans.append((s_m, a[i]))
            s_m -= a[i]
        else:
            ans.append((s_p, a[i]))
            s_p -= a[i]

        is_used[i] = True

ans.append((s_p, s_m))
ans_s = s_p - s_m

print(ans_s)
for ans_i in ans:
    print(*ans_i)
