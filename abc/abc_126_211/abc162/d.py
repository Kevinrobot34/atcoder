from bisect import bisect_left, bisect_right
n = int(input())
s = input()

color = 'RGB'
c_list = [[i for i in range(n) if s[i] == color[j]] for j in range(3)]
# print(*c_list, sep='\n')

ans1 = len(c_list[0]) * len(c_list[1]) * len(c_list[2])
ans2 = 0
for i in range(n):
    for j in range(1, n):
        if i + 2 * j >= n:
            continue
        if s[i] != s[i + j] and s[i + j] != s[i + 2 * j] and s[i +
                                                               2 * j] != s[i]:
            ans2 += 1

# print(ans1, ans2)
ans = ans1 - ans2
print(ans)
