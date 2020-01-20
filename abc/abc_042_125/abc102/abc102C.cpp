#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

int main() {
    int n;
    long long int a[200005], b;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
        a[i] -= i + 1;
    }

    sort(a, a+n);

    if (n % 2 == 1) b = a[(n - 1) /2];
    else b = (long long int)((a[n/2] + a[n/2 - 1]) / 2);

    long long int ans = 0;
    for (int i = 0; i < n; i++) {
        ans += abs(a[i] - b);
    }

    printf("%lld\n", ans);

    return 0;
}
