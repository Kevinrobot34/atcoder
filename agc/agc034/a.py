n, a, b, c, d = map(int, input().split())
s = '#' + input()

def check(l, r):
    return "##" not in s[l:r]

if c < d:
    if check(a, c) and check(b, d):
        print("Yes")
    else:
        print("No")
else: # c > d
    space = "..." in s[b-1:d+2]
    if space and check(a, c) and check(b, d):
        print("Yes")
    else:
        print("No")
