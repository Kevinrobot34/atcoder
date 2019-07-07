#include<bits/stdc++.h>
using namespace std;

int n, m, s, t;
vector<int> edge[100005];
vector<int> edge2[100005];

void dfs(int v0, int v, int k) {
  if (k == 0) {
    edge2[v0].push_back(v);
    return;
  }
  for (int i = 0; i < edge[v].size(); i++) {
    dfs(v0, edge[v][i], k-1);
  }
}

int main() {
  scanf("%d%d", &n, &m);

  for (int i = 0; i < m; i++) {
    int u, v;
    scanf("%d%d", &u, &v);
    u--;
    v--;
    edge[u].push_back(v);
  }
  for (int i = 0; i < n; i++) dfs(i, i, 3);
  for (int i = 0; i < n; i++) {
    printf("%d: ", i);
    for (int j = 0; j < edge[i].size(); j++) printf("%d ", edge[i][j]);
    printf("\n");
  }
  printf("\n");
  for (int i = 0; i < n; i++) {
    printf("%d: ", i);
    for (int j = 0; j < edge2[i].size(); j++) printf("%d ", edge2[i][j]);
    printf("\n");
  }

  scanf("%d%d", &s, &t);

  return 0;
}
