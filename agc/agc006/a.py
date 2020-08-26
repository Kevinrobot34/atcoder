n = int(input())
s = input()
t = input()

ans = s + t
for i in range(n):
    is_same = True
    for j in range(i, n):
        if s[j] != t[j - i]:
            is_same = False
            break
    if is_same:
        ans = s[:i] + t
        break

print(len(ans))
