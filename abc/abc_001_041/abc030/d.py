n, a = map(int, input().split())
k = int(input())
b = tuple(map(lambda x: int(x) - 1, input().split()))
a -= 1

words = [a]
is_used = [False] * n
while not is_used[words[-1]]:
    is_used[words[-1]] = True
    words.append(b[words[-1]])
# print(words)

idx = 0
while words[idx] != words[-1]:
    idx += 1

loop = len(words) - 1 - idx

if k < len(words):
    ans = words[k] + 1
else:
    ans = words[idx + (k - idx) % loop] + 1
print(ans)
