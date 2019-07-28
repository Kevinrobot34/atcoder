s = input()
t = input()

s = s * max(3, (len(t)*2) // len(s) + 1)


print()
print(s)
print(t)

index = s.find(t)
print(index)
