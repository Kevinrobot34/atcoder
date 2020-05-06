a, b, k, l = map(int, input().split())

ans1 = (k // l) * b + (k % l) * a
ans2 = ((k + l - 1) // l) * b
ans = min(ans1, ans2)
print(ans)
