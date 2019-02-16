#include <cstdio>
using namespace std;

int main() {
    long long int n, k;

    scanf("%lld%lld", &n, &k);

    long long int ans = 0;

    ans += (n/k) * (n/k) * (n/k);

    if (k % 2 == 0 && n >= k / 2) {
        long long int t = (n - k/2)/k + 1;
        ans += t*t*t;
    }

    printf("%lld\n", ans);

    return 0;
}
