s = input()

is_difficult = True
for i, si in enumerate(s):
    if i % 2 == 0 and (si < 'a' or 'z' < si):
        is_difficult = False
        break
    if i % 2 == 1 and (si < 'A' or 'Z' < si):
        is_difficult = False
        break

ans = 'Yes' if is_difficult else 'No'
print(ans)
