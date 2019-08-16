MOD = 1000000007
n = int(input())
s = [input() for _ in range(2)]

if s[0][0] == s[1][0]:
    ans = 3
    col = 1
else:
    ans = 6
    col = 2

while col < n:
    if s[0][col] == s[1][col]:
        if s[0][col - 1] == s[1][col - 1]:
            ans *= 2
        col += 1
    else:
        if s[0][col - 1] == s[1][col - 1]:
            ans *= 2
        else:
            ans *= 3
        col += 2

    ans %= MOD

print(ans)
