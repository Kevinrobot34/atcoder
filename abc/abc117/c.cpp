#include<cstdio>
#include<algorithm>

using namespace std;

int x[100005], dx[100005];
int main() {
    int n, m;

    scanf("%d%d", &n, &m);

    for (int i = 0; i < m; i++) scanf("%d", &x[i]);

    int ans = 0;

    if (n < m) {
        sort(x, x + m);
        for (int i = 0; i < m - 1; i++) dx[i] = x[i + 1] - x[i];
        sort(dx, dx + m - 1);

        for (int i = 0; i < m - n; i++) ans += dx[i];

    }

    printf("%d\n", ans);

    return 0;
}
