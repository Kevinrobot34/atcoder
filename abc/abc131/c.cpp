#include<cstdio>
#include<algorithm>

using namespace std;

long long int GCD(long long int a, long long int b) { return b ? GCD(b, a%b) : a; }

long long int func(long long int x, long long int c, long long int d) {
  long long int y = c * d / GCD(c, d);
  return (long long int)(x / c) + (long long int)(x / d) - (long long int) (x / y);
}

int main() {
  long long int a, b, c, d;

  scanf("%lld%lld%lld%lld", &a, &b, &c, &d);

  printf("%lld\n", b - a + 1  - (func(b, c, d) - func(a-1, c, d)) );
  return 0;
}
