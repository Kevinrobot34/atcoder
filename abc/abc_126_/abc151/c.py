n, m = map(int, input().split())

n_ac = [0] * n
n_wa = [0] * n
for i in range(m):
    p, s = input().split()
    p = int(p) - 1

    if s == 'AC':
        n_ac[p] += 1
    elif n_ac[p] == 0:
        n_wa[p] += 1

ans1 = ans2 = 0
for i in range(n):
    if n_ac[i] > 0:
        ans1 += 1
        ans2 += n_wa[i]

print(ans1, ans2)
