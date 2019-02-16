#include<cstdio>

int a[50];
int main() {
    int n, m;

    scanf("%d%d", &n, &m);

    for (int i = 0; i < n; i++) {
        int k, x;
        scanf("%d", &k);
        for (int j = 0; j < k; j++){
            scanf("%d", &x);
            a[x-1]++;
        }
    }

    int ans = 0;
    for (int i = 0; i < m; i++) {
        if (a[i] == n) ans++;
    }

    printf("%d\n", ans);

    return 0;
}
