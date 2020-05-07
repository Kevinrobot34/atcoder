#include<cstdio>

int b[3005][3005], w[3005][3005];
int b_cs[3005][3005], w_cs[3005][3005];
int n, k;

int func_b(int x, int y) {
  return b_cs[x + k][y + k] - b_cs[x + k][y] - b_cs[x][y + k] + b_cs[x][y];
}

int func_w(int x, int y) {
  return w_cs[x + k][y + k] - w_cs[x + k][y] - w_cs[x][y + k] + w_cs[x][y];
}


int main() {
  scanf("%d %d\n", &n, &k);
  int k2 = k * 2;
  for (int i = 0; i < n; i++){
    int x, y;
    char c;
    scanf("%d %d %c\n", &x, &y, &c);
    x %= k2;
    y %= k2;
    if (c == 'B') {
      b[x][y] += 1;
      if (x < k) b[x + k2][y] += 1;
      if (y < k) b[x][y + k2] += 1;
      if (x < k && y < k) b[x + k2][y + k2] += 1;
    } else {
      w[x][y] += 1;
      if (x < k) w[x + k2][y] += 1;
      if (y < k) w[x][y + k2] += 1;
      if (x < k && y < k) w[x + k2][y + k2] += 1;
    }
  }

  for (int i = 0; i <= k * 3 + 1; i++) {
    for (int j = 0; j <= k * 3 + 1; j++) {
      b_cs[i + 1][j + 1] = b_cs[i + 1][j] + b_cs[i][j + 1] - b_cs[i][j] + b[i][j];
      w_cs[i + 1][j + 1] = w_cs[i + 1][j] + w_cs[i][j + 1] - w_cs[i][j] + w[i][j];
    }
  }

  int ans = 0;
  for (int i = 0; i < k; i++) {
    for (int j = 0; j < k; j++) {
      int cand = 0;
      cand += func_b(i, j);
      cand += func_b(i + k, j + k);
      cand += func_w(i + k, j);
      cand += func_w(i, j + k);
      // printf("%d %d %d\n", i, j, cand);
      if (cand > ans) ans = cand;

      cand = 0;
      cand += func_w(i, j);
      cand += func_w(i + k, j + k);
      cand += func_b(i + k, j);
      cand += func_b(i, j + k);
      // printf("%d %d %d\n", i, j, cand);
      if (cand > ans) ans = cand;
    }
  }

  printf("%d\n", ans);

  return 0;
}
