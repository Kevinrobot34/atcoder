#include<stdio.h>
#include <string.h>

int a[100005];
long long int two[100005];
long long int three[100005];
long long int mod = 1000000007;

int main() {
  char s[100005];
  scanf("%s", s);

  int n = strlen(s);

  two[0] = 1;
  three[0] = 1;
  for (int i = 1; i <= n; i++) {
    two[i] = (two[i-1] * 2) % mod;
    three[i] = (three[i-1] * 3) % mod;
  }

  long long int ans = 0;
  int count = 0;
  for (int i = 0; i < n; i++) {
    if (s[i] == '1') {
      ans = (ans + three[n-i-1] * two[count]) % mod;
      count++;
    }
  }
  ans = (ans + two[count]) % mod;

  printf("%lld\n", ans);
  return 0;
}
