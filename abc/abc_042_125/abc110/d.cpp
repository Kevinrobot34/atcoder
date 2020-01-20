#include <cstdio>
#include <map>
#define MOD 1000000007 // 10^9 + 7
#define MAX 200000
using namespace std;

map<int,int> factorize(int m) {
    map<int, int> factor;

    while (m % 2 == 0) {
        factor[2]++;
        m /= 2;
    }

    int p = 3;
    while (p * p <= m) {
        if (m % p == 0) {
            factor[p]++;
            m /= p;
        } else {
             p += 2;
        }
    }

    if (m != 1) factor[m]++;
    return factor;
}

long long fac[MAX], finv[MAX], inv[MAX];

void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

long long COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}

int main() {
    int n,m;

    scanf("%d%d", &n, &m);

    map<int, int> factor = factorize(m);

    long long ans = 1;
    COMinit();
    for (auto it: factor) {
        //printf("%d %d\n", it.first, it.second);

        ans *= COM(it.second + n - 1, n - 1);
        ans %= MOD;
    }

    printf("%lld\n", ans);

    return 0;
}
