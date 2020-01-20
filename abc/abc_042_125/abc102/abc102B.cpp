#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

int main() {
    int n, ans;
    int a[105];

    scanf("%d", &n);

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            ans = max(ans, abs(a[i] - a[j]));
        }
    }

    printf("%d\n", ans);

    return 0;
}
