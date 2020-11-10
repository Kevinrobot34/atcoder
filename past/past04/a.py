from operator import itemgetter
a, b, c = map(int, input().split())
x = [(a, 'A'), (b, 'B'), (c, 'C')]
x.sort(key=itemgetter(0))
print(x[1][1])
