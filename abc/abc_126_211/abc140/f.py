import math
n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)


ans = "Yes"
for i in range(1, len(s)):
    par = i - 2**math.floor(math.log2(i))
    if s[par] <= s[i]:
        ans = "No"
        break

# print(s)
# print([i for i in range(len(s))])
# print([0] + [math.floor(math.log2(i)) + 1 for i in range(1, len(s))])
# print([0] + [i - 2**math.floor(math.log2(i)) for i in range(1, len(s))])
# for i in range(1, len(s)):


print(ans)
