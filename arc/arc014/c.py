from collections import Counter
n = int(input())
s = input()

ans = sum(v % 2 for v in Counter(s).values())
print(ans)
