s = input()
ans = sum(int(si) * ((-1)**i) for i, si in enumerate(s))
print(ans)
