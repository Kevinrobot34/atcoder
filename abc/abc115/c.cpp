#include<cstdio>
#include<algorithm>
using namespace std;

int h[100005];
int main() {
    int n, k;

    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) scanf("%d", &h[i]);

    sort(h, h + n);

    int ans = h[n-1] - h[0];
    for (int i = 0; i < n-k+1; i++) {
        ans = min(ans, h[i+k-1] - h[i]);
    }

    printf("%d\n", ans);

    return 0;
}
