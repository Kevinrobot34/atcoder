#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<list>
#include<queue>
#include<numeric>
#include<map>
#include<string>

using namespace std;

char m[2005][2005];
int vertical[2005][2005];
int horizontal[2005][2005];
int main() {
    int h, w;
    char s[2005];

    scanf("%d%d", &h, &w);
    for (int i = 0; i < w+2; i ++) {
      m[0][i] = '#';
      m[h+1][i] = '#';
    }
    for (int i = 0; i < h; i++) {
      scanf("%s", s);
      m[i+1][0] = '#';
      m[i+1][w+1] = '#';
      for (int j = 0; j < w; j++) m[i+1][j+1] = s[j];
    }
    // for (int i = 0; i < h+2; i++) printf(" %s\n", m[i]);

    for (int i = 1; i <= h; i++) {
      int c = 0;
      for (int j = 1; j <= w+1; j++) {
        if (m[i][j] == '#') {
          for (int k = c+1; k < j; k++) vertical[i][k] = j-c-1;
          c = j;
        }
      }
    }

    for (int i = 1; i <= w; i++) {
      int c = 0;
      for (int j = 1; j <= h+1; j++) {
        if (m[j][i] == '#') {
          for (int k = c+1; k < j; k++) horizontal[k][i] = j-c-1;
          c = j;
        }
      }
    }

    // for (int i = 1; i <= h; i++) {
    //   printf("  ");
    //   for (int j = 1; j <= w; j++) {
    //     printf("%d", horizontal[i][j]);
    //   }
    //   printf("\n");
    // }

    int ans = 1;
    for (int i = 1; i <= h; i++) {
      for (int j = 1; j <= w+1; j++) {
        if (m[i][j] == '#') continue;

        ans = max(ans, vertical[i][j]+horizontal[i][j]-1);
      }
    }
    printf("%d\n", ans);

    return 0;
}
