n, k = map(int, input().split())
d = input().split()

possible = False
while not possible:
    n_str = str(n)
    possible = True
    for di in d:
        if di in n_str:
            possible = False
            n += 1
            break

print(n)
