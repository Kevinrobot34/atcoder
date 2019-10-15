ai, ao, at, aj, al, a_s, a_z = map(int, input().split())

b = min(ai, aj, al)
ans1 = ao + min(1, b)*3 + ((ai - min(1, b)) // 2) * 2 + ((aj - min(1, b)) // 2) * 2 + ((al - min(1, b)) // 2) * 2
ans2 = ao + (ai // 2) * 2 + (aj // 2) * 2 + (al // 2) * 2

ans = max(ans1, ans2)

print(ans)
