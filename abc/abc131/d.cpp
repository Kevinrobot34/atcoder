#include<cstdio>
#include<algorithm>
#include<vector>
#include <iostream>

using namespace std;

struct task{
  int a, b;
  bool operator<( const task& right ) const {
    return (b == right.b) ? (a > right.a) : (b < right.b);
    // return (b == right.b) ? (a > right.a) : (b < right.b);
  };
};

int main() {
  int n;

  scanf("%d", &n);
  vector<task> v(n);
  int a, b;
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &v[i].a, &v[i].b);
  }

  sort(v.begin(), v.end());

  int t = 0;
  int i;
  for (i = 0; i < n; i++) {
    t += v[i].a;
    if ( t > v[i].b ) break;
    // printf("%d %d\n", v[i].a, v[i].b);
  }
  printf("%s\n", (i==n) ? "Yes" : "No");

  return 0;
}
