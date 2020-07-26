target_string = {
    '####.##.##.####': '0',
    '.#.##..#..#.###': '1',
    '###..#####..###': '2',
    '###..####..####': '3',
    '#.##.####..#..#': '4',
    '####..###..####': '5',
    '####..####.####': '6',
    '###..#..#..#..#': '7',
    '####.#####.####': '8',
    '####.####..####': '9',
}

n = int(input())
t = [''] * n
for _ in range(5):
    s_i = input()
    for j in range(n):
        t[j] += s_i[4 * j + 1:4 * j + 4]

ans = ''.join(map(lambda t_j: target_string[t_j], t))
print(ans)