#include<cstdio>
#include<algorithm>

using namespace std;

int w[110];
int w_cum[110];
int main() {
  int n;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%d", &w[i]);
    if (i == 0) w_cum[i] = w[i];
    else w_cum[i] = w_cum[i-1] + w[i];
  }

  int ans = w_cum[n-1];
  for (int i = 0; i < n; i++) {
    int s2 = w_cum[n-1] - w_cum[i];
    ans = min(ans, abs(s2 - w_cum[i]));
  }
  printf("%d\n", ans);

  return 0;
}
