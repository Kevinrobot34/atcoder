import math

d, g = map(int, input().split())
g = g // 100
p = [0]*d
c = [0]*d
for i in range(d):
    p[i], c[i] = map(int, input().split())
    c[i] = c[i] // 100

ans = sum(p)

for bit in range(1<<d):
    tmp_ans = 0
    tmp_score = 0
    for i in range(d):
        if (bit >> i) & 1 == 1:
            tmp_ans += p[i]
            tmp_score += (i+1) * p[i] + c[i]

    for i in reversed(range(d)):
        if (bit >> i) & 1 == 0 and tmp_score < g:
            if g - tmp_score > (i+1) * p[i]:
                tmp_ans += p[i]
                tmp_score += (i+1) * p[i] + c[i]
            else:
                n = math.ceil( (g - tmp_score) / (i+1) )
                tmp_ans += n
                tmp_score += (i+1) * n

    ans = min(ans, tmp_ans)

print(ans)
