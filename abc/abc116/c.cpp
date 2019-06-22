#include<cstdio>
#include<algorithm>
using namespace std;

int h[105];

int func(int l, int r, int m) {
    if (l >= r) return 0;

    int i;
    for (i = l; i < r; i++) {
        if (h[i] == m) {
            return func(l, i, m) + func(i + 1, r, m);
        }
    }
    if (i == r) {
        return func(l, r, m + 1) + 1;
    }
}

int main() {
    int n;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &h[i]);

    printf("%d\n", func(0, n, 0));

    return 0;
}
