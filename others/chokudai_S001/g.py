MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))
ans = 0
for ai in a:
    ans = (ans * pow(10, len(str(ai))) + ai) % MOD
print(ans)
