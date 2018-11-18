s = str(input())
cost = 700
for i in range(3):
    if s[i] == 'o':
        cost += 100
print(cost)
