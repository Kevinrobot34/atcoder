#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

struct UnionFind {
  vector<int> par;
  UnionFind(int N) : par(N) {
    for (int i = 0; i < N; i++) par[i] = i;
  }

  int find(int x) {
    if (par[x] != x) par[x] = find(par[x]); // contruction
    return par[x];
  }

  void unite(int x, int y) {
    x = find(x);
    y = find(y);
    par[x] = y;
  }

  bool same(int x, int y) { return find(x) == find(y); }
};

int p[100005];
int main() {
  int n, m;

  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%d", &p[i]);
    p[i]--;
  }

  UnionFind uf(n);
  for (int i = 0; i < m; i++) {
    int x, y;
    scanf("%d%d", &x, &y);
    uf.unite(x-1, y-1);
  }

  int ans = 0;
  for (int i = 0; i < n; i++) if (uf.same(i, p[i])) ans++;

  printf("%d\n", ans);

  return 0;
}
