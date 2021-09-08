n = int(input())
a = []
a1 = a2 = 0
for i in range(n):
    ai = int(input())
    a.append(ai)
    if ai > a1:
        a1, a2 = ai, a1
    elif ai > a2:
        a2 = ai

for i in range(n):
    if a[i] == a1:
        print(a2)
    else:
        print(a1)
