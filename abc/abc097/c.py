s = input()
k = int(input())

substr = []
for n in range(1, k+1):
    for i in range(len(s)-n+1):
        substr.append(s[i:i+n])

substr = list(set(substr))
substr.sort()
print(substr[k-1])
