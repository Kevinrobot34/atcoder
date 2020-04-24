x = input()

x = x.replace('ch', 'C')
x = set(list(x))

target_char = {'C', 'o', 'k', 'u'}
ans = 'YES'
for xi in x:
    if xi not in target_char:
        ans = 'NO'
        break

print(ans)
