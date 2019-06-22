#include<stdio.h>
#include <string.h>

int graph[105][105];
int main() {
  int n, k;

  scanf("%d%d", &n, &k);

  if (k > (n-1)*(n-2)/2) {
    printf("-1\n");
  } else {
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) graph[i][j] = 0;
    for (int i = 1; i < n; i++) {
      graph[0][i] = 1;
    }
    int m = (n-1)*(n-2)/2 - k;
    int x = 1;
    int y = 2;
    int n_e = m + n - 1;
    while (m--) {
      graph[x][y] = 1;
      y++;
      if (y % n == 0) {
        x++;
        y = x+1;
      }
    }

    printf("%d\n", n_e);
    for (int i = 0; i < n; i++) for (int j = i+1; j < n; j++) if(graph[i][j] == 1) printf("%d %d\n", i+1, j+1);
  }

  return 0;
}
