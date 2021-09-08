n = 1000
with open('abc/abc_126_/abc160/test.txt', 'w') as writer:
    writer.write(f'{n}\n')
    for i in range(1, n):
        writer.write(f'{i} {i + 1}\n')
