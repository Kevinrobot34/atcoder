k = int(input())
s = input()
if len(s) <= k:
    ans = s
else:
    ans = s[:k] + '...'
print(ans)
