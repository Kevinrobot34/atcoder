n = int(input())
a = list(map(int, input().split()))

a_max = max(a)
ans = 0
ans_cnt = 0
for k in range(2, a_max + 1):
    cnt = sum(1 for ai in a if ai % k == 0)
    if ans_cnt < cnt:
        ans = k
        ans_cnt = cnt

print(ans)
