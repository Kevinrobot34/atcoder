from collections import Counter
w = input()

d = Counter(w)
ans = "Yes"
for c in d:
    if d[c] % 2 == 1:
        ans = "No"
        break

print(ans)
