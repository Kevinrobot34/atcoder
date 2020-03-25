s = input()
k = int(input())

cand = set()
for i in range(len(s) - k + 1):
    cand.add(s[i:i + k])

ans = len(cand)
print(ans)
