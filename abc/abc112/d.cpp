#include <cstdio>

int main() {
    int n, m;

    scanf("%d%d", &n, &m);

    int p = m / n;
    while (m % p != 0) p--;

    printf("%d\n", p);
}
