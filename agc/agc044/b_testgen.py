import random
n = int(input())
print(n)
p = list(range(1, n**2 + 1))
random.shuffle(p)
print(*p)
