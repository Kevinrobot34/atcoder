def check(w1, w2):
    if w1[0] == '*':
        return False

    if len(w1) != len(w2):
        return False
    is_same = True
    for i in range(len(w1)):
        if w2[i] != '*' and w2[i] != w1[i]:
            is_same = False
            break
    return is_same


s = input().split()
n = int(input())
for _ in range(n):
    t = input()
    for i in range(len(s)):
        if check(s[i], t):
            s[i] = '*' * len(s[i])

ans = ' '.join(s)
print(ans)
