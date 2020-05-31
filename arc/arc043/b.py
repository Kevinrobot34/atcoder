from bisect import bisect_left, bisect_right
n = int(input())
d = [int(input()) for _ in range(n)]
d.sort()

MOD = 10**9 + 7

index_br = [bisect_right(d, d[i] // 2) for i in range(n)]
# print(d)
# print(index_br)

cnt1 = list(range(n + 1))
# print(cnt1)
for _ in range(3):
    cnt2 = [0] * n
    for i in range(n):
        if index_br[i] > 0:
            cnt2[i] = cnt1[index_br[i]]

    cnt1 = [0] * (n + 1)
    for i in range(n):
        cnt1[i + 1] = (cnt1[i] + cnt2[i]) % MOD
    # print(cnt1)

ans = cnt1[-1]
print(ans)
