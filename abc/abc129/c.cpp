#include<cstdio>
#include<algorithm>

using namespace std;

int a[100005];
long long int fibo[100005];
long long int mod = 1000000007;

int main() {
  int n, m;
  scanf("%d%d", &n, &m);

  fibo[0] = 1;
  fibo[1] = 1;
  for (int i = 2; i <= n; i++) {
    fibo[i] = fibo[i-1] + fibo[i-2];
    fibo[i] = fibo[i] % mod;
  }

  long long int ans = 1;
  int b = -1;
  for (int i = 0; i < m; i++) {
    scanf("%d", &a[i]);
    if (a[i] == b) continue;

    if (a[i] - b - 2 >= 0) {
      ans = (ans * fibo[a[i] - b - 2]) % mod;
    } else {
      ans = 0;
    }
    b = a[i];
  }
  ans = (ans * fibo[n+1 - b - 2]) % mod;

  printf("%lld\n", ans);

  return 0;
}
