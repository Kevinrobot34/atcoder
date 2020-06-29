b = list(map(int, input().split()))
n = int(input())
a = [input() for _ in range(n)]

d = str.maketrans({str(b[i]): str(i) for i in range(10)})
a.sort(key=lambda x: int(x.translate(d)))
print(*a, sep='\n')
