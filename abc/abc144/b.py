n = int(input())


def check():
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                return True
    return False


if check():
    print("Yes")
else:
    print("No")
