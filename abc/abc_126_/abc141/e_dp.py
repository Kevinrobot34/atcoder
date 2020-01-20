n = int(input())
s = input()

ans = 0
for i in range(1, n):
    cnt = 0
    for j in range(n-i):
        if s[i+j] == s[j]:
            cnt += 1
        else:
            ans = max(ans, min(cnt, i))
            cnt = 0

        if cnt >= i:
            break
    ans = max(ans, min(cnt, i))

print(ans)
