n = int(input())

if n % 7 == 0 or n % 4 == 0:
    print("Yes")
elif n >= 4 and n % 7 == 4:
    print("Yes")
elif n >= 8 and n % 7 == 1:
    print("Yes")
elif n >= 12 and n % 7 == 5:
    print("Yes")
elif n >= 16 and n % 7 == 2:
    print("Yes")
elif n >= 20 and n % 7 == 6:
    print("Yes")
elif n >= 24 and n % 7 == 3:
    print("Yes")
else:
    print("No")
