n = int(input())
b = list(map(int, input().split()))

impossible = False
for i in range(n):
    if b[i] > i+1:
        impossible = True
        break

if impossible:
    print("-1")
else:
    pass
    ans = []
    while b:
        # print(b)
        for i in reversed(range(len(b))):
            if b[i] == i+1:
                ans.append(b.pop(i))
                break
    for i in reversed(range(n)):
        print(ans[i])
