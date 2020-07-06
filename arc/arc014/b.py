n = int(input())
words = [input() for _ in range(n)]

ans = 'DRAW'
words_set = set([words[0]])
for i in range(1, n):
    if words[i] in words_set or words[i][0] != words[i - 1][-1]:
        ans = 'WIN' if i % 2 == 1 else 'LOSE'
        break
    words_set.add(words[i])

print(ans)
