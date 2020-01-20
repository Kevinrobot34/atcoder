#include <bits/stdc++.h>
using namespace std;

struct sushi{
  int t, d;
  bool operator<( const task& right ) const {
    return (b == right.b) ? (a > right.a) : (b < right.b);
    // return (b == right.b) ? (a > right.a) : (b < right.b);
  };
};

int t[100005], d[100005];
int main() {
  int n, k;

  scanf("%d%d", &n, &k);
  vector<sushi> v(n);
  int a, b;
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &v[i].a, &v[i].b);
  }



  return 0;
}
