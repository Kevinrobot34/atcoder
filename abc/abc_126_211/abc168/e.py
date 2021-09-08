from collections import defaultdict

MOD = 1000000007
n = int(input())


def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)


# GCD(-2, 4)

iwasi_cnt = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    if b < 0:
        a, b = -a, -b
    # iwasi.append((a, b))

    g = GCD(abs(a), abs(b))
    if g == 0:
        # (0, 0)
        iwasi_cnt[(a, b)] += 1
    else:
        iwasi_cnt[(a // g, b // g)] += 1

iwasi_cnt = dict(iwasi_cnt)
# print(iwasi_cnt)
cand = []
cnt0 = 0
for (a, b), v in iwasi_cnt.items():
    if a == 0 and b == 0:
        cnt0 += v
    else:
        if (-b, a) in iwasi_cnt:
            m = iwasi_cnt[(-b, a)]
            cand.append((v, m))
        elif (b, -a) not in iwasi_cnt:
            cand.append((v, ))

# print(*cand, sep='\n')
ans = 1
for i in range(len(cand)):
    if len(cand[i]) == 1:
        x = cand[i][0]
        ans *= pow(2, x, MOD)
        ans %= MOD
    else:
        x, y = cand[i]
        ans *= (MOD + pow(2, x, MOD) + pow(2, y, MOD) - 1) % MOD
        ans %= MOD

ans -= 1  # 0匹を取り除く
ans %= MOD
ans += cnt0  # (0, 0)を追加
ans %= MOD
print(ans)
