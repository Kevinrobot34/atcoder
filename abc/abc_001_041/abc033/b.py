n = int(input())

name_cand = ""
p_cand = -1
p_sum = 0
for _ in range(n):
    name, p = input().split()
    p = int(p)
    p_sum += p
    if p > p_cand:
        p_cand = p
        name_cand = name

if p_cand * 2 <= p_sum:
    ans = "atcoder"
else:
    ans = name_cand

print(ans)
