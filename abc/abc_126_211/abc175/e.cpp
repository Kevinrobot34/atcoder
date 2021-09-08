#include <cstdio>
#include <bits/stdc++.h>
using namespace std;

long long int items[3005][3005];
long long int dp[3005][3005][4];

int main() {
  int r, c, k;
  scanf("%d%d%d", &r, &c, &k);
  for (int l = 0; l < k; l ++) {
    int i, j, v;
    scanf("%d%d%d", &i, &j, &v);
    items[i][j] = v;
  }
  for (int i = 1; i <= r; i++) {
    for (int j = 1; j <= c; j++) {
      for (int m = 0; m < 4; m++) {
        dp[i][j][m] = max(dp[i - 1][j][3], dp[i][j - 1][m]);
      }
      if (items[i][j] > 0) {
        for (int m = 2; m >= 0; m--) {
          dp[i][j][m + 1] = max(dp[i][j][m + 1], dp[i][j][m] + items[i][j]);
        }
      }
    }
  }

  printf("%lld\n", dp[r][c][3]);
  return 0;
}
