from collections import Counter
s = input()
cnt = Counter(s)
ans = cnt.most_common(1)[0][0]
print(ans)
