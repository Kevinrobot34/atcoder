n = int(input())
c = input()

d = {'1': 0, '2': 0, '3': 0, '4': 0}
for i in range(n):
    d[c[i]] += 1

print(max(d.values()), min(d.values()))
