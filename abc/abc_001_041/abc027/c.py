n = int(input())

x = 1
cnt = 0
while x <= n:
    if cnt % 2 == 1:
        x = 2 * x
    else:
        x = 2 * x + 1

    cnt += 1

if cnt % 2 == 1:
    ans = "Aoki"
else:
    ans = "Takahashi"

print(ans)
