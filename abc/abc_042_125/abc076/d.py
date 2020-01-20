n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

t_cs = [0] * (n+1)
for i in range(n):
    t_cs[i+1] = t_cs[i] + t[i]

v_l = [t_cs[i] for i in range(n)]
v_r = [t_cs[n] - t_cs[i+1] for i in range(n)]
for i in range(n):
    v_l[i] = min(v_l[i], v[i])
    v_r[i] = min(v_r[i], v[i])

    for j in range(i, n):
        v_l[j] = min(v_l[j], v[i] + (t_cs[j] - t_cs[i]))
        if j > i:
            v_l[j] = min(v_l[j], v[i] + (t_cs[j] - t_cs[i+1]))

    for j in range(i):
        v_r[j] = min(v_r[j],
                     v[i] + (t_cs[i+1] - t_cs[j+1]),
                     v[i] + (t_cs[i]   - t_cs[j+1]))


print(v)
print(v_l)
print(v_r)
