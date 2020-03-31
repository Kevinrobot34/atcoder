l1, l2, l3 = map(int, input().split())
if l1 == l2:
    ans = l3
elif l2 == l3:
    ans = l1
else:
    ans = l2
print(ans)
