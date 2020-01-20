n = int(input())
s = input()

cs = [0] * (n+1)
for i in range(n):
    cs[i+1] = cs[i]
    if s[i] == 'E':
        cs[i+1] += 1

ans = n
for i in range(n):
    e_left = cs[i]
    e_right = cs[n] - cs[i+1]
    # print(i, e_left, e_right)
    ans = min(ans, (i - e_left) + e_right)

print(ans)
