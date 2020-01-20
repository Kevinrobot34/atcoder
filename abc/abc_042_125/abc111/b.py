n = input()

while len(set(n)) > 1:
    n = str(int(n) + 1)

print(n)
