n = int(input())
s = input()

if n % 2 == 0:
    if s[:n // 2] + s[:n // 2] == s:
        ans = "Yes"
    else:
        ans = "No"
else:
    ans = "No"

print(ans)
