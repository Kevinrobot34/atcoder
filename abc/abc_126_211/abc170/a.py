x = list(map(int, input().split()))

for i in range(len(x)):
    if x[i] != i + 1:
        print(i + 1)
