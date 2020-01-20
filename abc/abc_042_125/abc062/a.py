x, y = map(int, input().split())

g1 = [1, 3, 5, 7, 8, 10, 12]
g2 = [4, 6, 9, 11]
if x in g1 and y in g1:
    ans = "Yes"
elif x in g2 and y in g2:
    ans = "Yes"
else:
    ans = "No"

print(ans)
