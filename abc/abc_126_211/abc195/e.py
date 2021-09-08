n = int(input())
s = input()
x = input()
BASE = 10
LUCKY = 7

# dp[i][j] = (iラウンド目までで余りがjの時、高橋くんが勝確かどうか)
dp = [[False] * LUCKY for _ in range(n + 1)]
dp[n][0] = True

for i in reversed(range(n)):
    for j in range(LUCKY):
        cand1 = (j * BASE) % LUCKY  # 0を追加
        cand2 = (j * BASE + int(s[i])) % LUCKY  # s[i]を追加

        if x[i] == 'T':
            dp[i][j] = dp[i + 1][cand1] or dp[i + 1][cand2]
        else:
            dp[i][j] = dp[i + 1][cand1] and dp[i + 1][cand2]

ans = 'Takahashi' if dp[0][0] else 'Aoki'
# print(*dp, sep='\n')
print(ans)
