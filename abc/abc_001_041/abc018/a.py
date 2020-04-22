a = [int(input()) for _ in range(3)]
a_sort = sorted(a, reverse=True)

ans = [a_sort.index(ai) + 1 for ai in a]
print(*ans, sep='\n')
