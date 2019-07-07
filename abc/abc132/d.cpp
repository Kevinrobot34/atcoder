#include<bits/stdc++.h>
using namespace std;

#define MOD 1000000007 // 10^9 + 7
#define MAX 510000

long long int fac[MAX], finv[MAX], inv[MAX];

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

long long int COM(int n, int k){
  if (n < k) return 0;
  if (n < 0 || k < 0) return 0;
  return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}


int main() {
  // 前処理
  COMinit();

  int n, k;

  scanf("%d%d", &n, &k);

  for (int i = 1; i <= k; i++) {
    long long int ans = ( COM(k-1, i-1) * COM(n-k+1, i) ) % MOD;
    printf("%lld\n", ans);
  }

  return 0;
}
