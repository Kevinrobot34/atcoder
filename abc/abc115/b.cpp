#include<cstdio>
#include<algorithm>
using namespace std;

int main() {
    int n, p, p_max;

    scanf("%d", &n);

    int ans = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &p);
        ans += p;
        p_max = max(p_max, p);
    }
    ans -= p_max / 2;

    printf("%d\n", ans);

    return 0;
}
