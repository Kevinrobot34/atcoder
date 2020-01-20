n = int(input())
restaurant = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    restaurant.append((s, p, i+1))
restaurant.sort(key=lambda x: (x[0], -x[1]))

for i in range(n):
    print(restaurant[i][2])
