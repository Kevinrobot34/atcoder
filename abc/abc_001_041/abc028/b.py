s = input()
ans = [s.count(chr(ord('A') + i)) for i in range(6)]
print(*ans)
