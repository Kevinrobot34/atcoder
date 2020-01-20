n = int(input())
a = list(map(int, input().split()))

x, y, z = 0, 0, 0
for i in range(n):
    if a[i] % 4 == 0:
        x += 1
    elif a[i] % 2 == 0:
        y += 1
    else:
        z += 1

if x >= z:
    print("Yes")
elif x == z - 1 and y == 0:
    print("Yes")
else:
    print("No")
