a, b, n = map(int, input().split())
x = str(input())

for i in range(len(x)):
    if x[i] == 'S':
        if a > 0:
            a -= 1
    elif x[i] == 'C':
        if b > 0:
            b -=1
    else:
        if a > b:
            a -= 1
        elif a < b:
            b -= 1
        elif a > 0:
            a -= 1

print(a)
print(b)
