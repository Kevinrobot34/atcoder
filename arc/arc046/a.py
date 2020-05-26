n = int(input())

x = 1
zorome = []
while len(zorome) < n:
    if len(set(list(str(x)))) == 1:
        zorome.append(x)
    x += 1

print(zorome[-1])
