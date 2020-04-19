from collections import Counter
n, k = map(int, input().split())
s = input()
s_cnt = Counter(list(s))
s_char = sorted(list(s))

print(s_char)
print(s_cnt)
s_cnt['a'] -= 1
print(s_cnt)

ans = ''
j = 0
for i in range(n):
